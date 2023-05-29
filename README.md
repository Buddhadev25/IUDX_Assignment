# IUDX_Assignment

## Assignment-1:
```
Write a application/use your existing/easy to do projects from internet with following criteria:
a. A basic HTTP web application in any language which takes some input through an API endpoint and process it and 
store the data to db
b. The database can be mysql, psql, mongodb etc.
```
### Solution
http://127.0.0.1:5000/ web application takes input through http://127.0.0.1:5000/weather/{Latitude}/{Longitude} 
API ENDPOINT and processing the coordinates using openweathermap and storing the location and current weather to MYSQL database. 

#### steps:
  ```
  1. https://github.com/Buddhadev25/IUDX_Assignment/blob/master/Assignment-1/main.py Flask API server developed, where http://127.0.0.1:5000/(route root) rendering Weather.html file. 
  2. When ENDPOINT sends Latitude, Longitude as input, weather function is taking these inputs and start processing 
  through https://openweathermap.org/api and calculate current weather and location. 
  3. Then current weather and location details are passed to store function, this function will store these 
  information in MYSQL database. 
  4. Created MYSQl database in my local server named webapi and table named weather
```
Screenshots are attached. 

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
Here I am containerizing Postgres and todo-list components using docker-compose. The aim is to add New Item in 
the todo-list web interface and store the item in Postgres database. 

#### Steps:
````
1. Followed https://docs.docker.com/engine/install/ubuntu/ docs for Install Docker Engine
2. Developed Assignment-2/docker-compose.yaml and postgres-connection.json file
3. I am using postgres 11.5 docker image, and exposing 5433 port, and using volume /data/postgress for data persistance purpose. 
5. todo-list container exposed on 8050 port, and connecting the database using environment variables and 
postgres secrets file /app/config/secrets.json
6. Sending postgres database secrets as a file named postgress-connection.json, this can help to manage 
any sensitive data and when we dont wants to store credentials in version control systems like Gitlab or Github.
7. Used docker compose up command to run multi-container Docker application.
````
Screenshots are attached. 

![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/e6790709-dbf6-43f9-a16f-f1877ec0185a)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/b0283a09-c877-483b-bd4f-a3f32c647a05)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/c3294f53-600d-4e7e-acc7-dcde7b131e87)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/6460b873-d193-4196-826f-6f043ad6b621)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/c6736764-7dcf-4cbb-a7a7-490d0f2d1fc2)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/b88bb470-1d9a-4c91-98ec-8ee2453f48c7)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/d1690a4c-1a0b-48ba-b668-6486b05c347e)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/c0e6cc33-44c3-48a6-a467-2f0a6c38e504)

## Assignment-3:
```
Containerise and deploy the two components in local K8s minikube cluster (using kubectl only):
a) Please see the instructions on how to create a minikube on a local machine at
https://github.com/datakaveri/iudx-deployment/tree/master/K8s-deployment/K8s-cluster/minikube .
b) Add auto scaling to any one of the components - web server or database.
c) Expose the web application in K8s to outside world, so that it can be
accessed through something like http://localhost:35622/xyz/
```
### Solution


#### Steps:






![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/00538491-d067-447f-9ec4-a85a1ad280cd)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/29dba80b-fb64-453a-925e-51062045924a)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/b4677c3f-e985-4752-8215-0ba6b807e276)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/5270d5db-aa49-4612-b00d-7d83e7c2c395)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/c4297850-f259-4289-8a1a-dadb6a1a8d32)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/f15510e6-a075-40af-815f-59bd5812f137)

