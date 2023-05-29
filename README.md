# IUDX_Assignment

## Assignment-1:
Write a application/use your existing/easy to do projects from internet with following criteria:
```
a. A basic HTTP web application in any language which takes some input through an API endpoint and process it and store the data to db
b. The database can be mysql, psql, mongodb etc.
```
### Solution
http://127.0.0.1:5000/ web application takes input through http://127.0.0.1:5000/weather/{Latitude}/{Longitude} API ENDPOINT and processing the coordinates using openweathermap and storing the location and current weather to MYSQL database. 

steps:
  ```
  1. https://github.com/Buddhadev25/IUDX_Assignment/blob/master/Assignment-1/main.py Flask API server developed, where http://127.0.0.1:5000/(route root) rendering Weather.html file. 
  2. When ENDPOINT sends input, weather function is taking those input and start 
  

