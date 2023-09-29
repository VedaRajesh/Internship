# Internship
# TO RUN THIS CODE #

1. Save it to a Python file (e.g., app.py).
2. Make sure you have Flask installed (pip install flask).
3. Run the application with python app.py.
4. Use a tool like curl, Postman, or a web browser to interact with the endpoints.

* POST to add climate data:
  ```ruby
   curl -X POST -H "Content-Type: application/json" -d '{"area_code": 100, "climate_type": "hot", "temperature": 30, "humidity": 2, "chances_of_rain": 0.2}' http://localhost:5000/add_climate_data
  ```
* GET to fetch all records:

  ```ruby
   curl http://localhost:5000/get_all_records
  ```
* GET to fetch records by area code:
  ``` ruby
    curl http://localhost:5000/get_records_by_area/100
  ```
 * GET to fetch records by area code and climate type:
   ```ruby
      curl http://localhost:5000/get_records_by_climate/100/hot
   ```
  Make sure to adapt the code and endpoints to your specific requirements and integrate proper error handling, security, and validation as needed for a production environment. 
 
