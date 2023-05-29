# IUDX_Assignment

## Assignment-1:
Write a application/use your existing/easy to do projects from internet with following criteria:
```
a. A basic HTTP web application in any language which takes some input through an API endpoint and process it and store the data to db
b. The database can be mysql, psql, mongodb etc.
```
### Solution
http://127.0.0.1:5000/ web application takes input through http://127.0.0.1:5000/weather/{Latitude}/{Longitude} API ENDPOINT and processing the coordinates using openweathermap and storing the location and current weather to MYSQL database. 

#### steps:
  ```
  1. https://github.com/Buddhadev25/IUDX_Assignment/blob/master/Assignment-1/main.py Flask API server developed, where http://127.0.0.1:5000/(route root) rendering Weather.html file. 
  2. When ENDPOINT sends Latitude, Longitude as input, weather function is taking these inputs and start processing through https://openweathermap.org/api and calculate current weather and location. 
  3. Then current weather and location details are passed to store function, this function will store these information in MYSQL database. 
  4. Created MYSQl database in my local server named webapi and table named weather
```
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/74a21d48-af97-4bc3-ab2d-0fcb7250adb2)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/66fec199-31fd-4299-b2ca-0aaea535f0dc)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/5ec303dd-b3df-431e-a8b2-5cb314958fc7)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/5bc3db47-4c5d-4a17-9431-f122371406ba)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/4c93e0fb-93ae-4f70-a465-9f35b1e1bb2d)

## Assignment-2:
```
Containerise and deploy the two components in local machine using docker-compose
a) Refer docker docs and docker-compose docs
b) Expose the web application in docker to outside world, so that it can be accessed through something like http://localhost:35622/xyz/
```
### Solution
