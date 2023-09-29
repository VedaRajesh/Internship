from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///climate_data.db'
db = SQLAlchemy(app)


class ClimateData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_code = db.Column(db.Integer)
    climate_type = db.Column(db.String(20))
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    chances_of_rain = db.Column(db.Float)

    def __init__(self, area_code, climate_type, temperature, humidity, chances_of_rain):
        self.area_code = area_code
        self.climate_type = climate_type
        self.temperature = temperature
        self.humidity = humidity
        self.chances_of_rain = chances_of_rain


# Create the database tables
with app.app_context():
    db.create_all()


# Endpoint to add climate data
@app.route('/add_climate_data', methods=['POST'])
def add_climate_data():
    data = request.json
    area_code = data.get('area_code')
    climate_type = data.get('climate_type')
    temperature = data.get('temperature')
    humidity = data.get('humidity')
    chances_of_rain = data.get('chances_of_rain')

    if None in (area_code, climate_type, temperature, humidity, chances_of_rain):
        return jsonify({'message': 'All fields are required'}), 400

    climate_data = ClimateData(area_code, climate_type, temperature, humidity, chances_of_rain)
    db.session.add(climate_data)
    db.session.commit()
    return jsonify({'message': 'Climate data added successfully'}), 201


# Endpoint to fetch all saved records
@app.route('/get_all_records', methods=['GET'])
def get_all_records():
    climate_data = ClimateData.query.all()
    return jsonify([record.__dict__ for record in climate_data]), 200


# Endpoint to fetch records of a particular area
@app.route('/get_records_by_area/<int:area_code>', methods=['GET'])
def get_records_by_area(area_code):
    climate_data = ClimateData.query.filter_by(area_code=area_code).all()
    if not climate_data:
        return jsonify({'message': 'No records found for this area'}), 404
    return jsonify([record.__dict__ for record in climate_data]), 200


# Endpoint to fetch records of a particular climate of a particular area
@app.route('/get_records_by_climate/<int:area_code>/<string:climate_type>', methods=['GET'])
def get_records_by_climate(area_code, climate_type):
    climate_data = ClimateData.query.filter_by(area_code=area_code, climate_type=climate_type).all()
    if not climate_data:
        return jsonify({'message': 'No records found for this area and climate'}), 404
    return jsonify([record.__dict__ for record in climate_data]), 200


if __name__ == '__main__':
    app.run(debug=True)
