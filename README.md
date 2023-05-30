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
  - https://github.com/Buddhadev25/IUDX_Assignment/blob/master/Assignment-1/main.py Flask API server developed, where http://127.0.0.1:5000/(route root) rendering Weather.html file. 
  - When ENDPOINT sends Latitude, Longitude as input, weather function is taking these inputs and start processing 
  through https://openweathermap.org/api and calculate current weather and location. 
  - Then current weather and location details are passed to store function, this function will store these 
  information in MYSQL database. 
  - Created MYSQl database in my local server named webapi and table named weather

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

- Followed https://docs.docker.com/engine/install/ubuntu/ docs for Install Docker Engine
- Developed Assignment-2/docker-compose.yaml and postgres-connection.json file
- I am using postgres 11.5 docker image, and exposing 5433 port, and using volume /data/postgress for data persistance purpose. 
- todo-list container exposed on 8050 port, and connecting the database using environment variables and 
postgres secrets file /app/config/secrets.json
- *** Sending postgres database secrets as a file named postgress-connection.json, this can help to manage 
any sensitive data and when we dont wants to store credentials in version control systems like Gitlab or Github. ***
- Used docker compose up command to run multi-container Docker application.

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
I am containerizing and deploying mongo database and mongo-express web admin interfaces in local K8s minikube cluster. Adding data in mongo-express and the data is stored in mongo database. 

#### Steps:

- Followed https://minikube.sigs.k8s.io/docs/start/ docs for local Kubernetes cluster(minikube) installation
- mongo-secret.yaml file contains the environments of mongo db. username and password are in base64. 
When we don't want to store credentials in version control systems we use Kubernetes secrets file.  
- mongo.yaml is type deployment and mongo db username, and password is referenced from mongodb-secret. 
Also, an internal service is created so that other pods can communicate with mongo db pod. 
- mongo-configmap.yaml contain mongo db server details, mongodb-service is the service of mongo db.
- Mongo express is a frontend app that will access the mongo DB. To access DB, I configured DB url in pod template. 
mongo username and password is referenced from the same mongodb-secret. 
The value of ME_CONFIG_MONGODB_SERVER is referenced from mongodb-configmap. 
The type of this service is LoadBalancer and LoadBalancer accepts external requests by assigning 
the service with an external IP address. 30000 Nodeport is exposed, so that we can access the service from the browser.  
- Implemented Horizontal Pod Autoscaler(HPA) for adjusts the number of replicas of mongo-express application. Here HPA maintains between 2 and 10 replicas of the pods controled by HPA. Target of 50% is the average CPU utilization that HPA needs to maintain alltime. 

Screenshots are attached. 

![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/00538491-d067-447f-9ec4-a85a1ad280cd)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/29dba80b-fb64-453a-925e-51062045924a)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/b4677c3f-e985-4752-8215-0ba6b807e276)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/c4297850-f259-4289-8a1a-dadb6a1a8d32)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/53589365-cfd7-40c4-87ea-a8adbd5b0520)
![image](https://github.com/Buddhadev25/IUDX_Assignment/assets/104052706/f4f302f7-af3c-4a94-a1de-97a07d032157)

> Since Metrics Server is installed on cluster, current CPU utilization is not unknown by kubernetes. 
