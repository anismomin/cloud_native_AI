# Cloud Native AI

# Development Stack

    1. Modern Python 
        https://www.youtube.com/watch?v=rwDHhx76MMg&list=PL0vKVrkG4hWrEujmnC7v2mSiaXMV_Tfu0
        
    2. FastAPI - Framerwork with AI applications
        - https://www.youtube.com/watch?v=ckXDNS2iRiY&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=2&pp=iAQB

    3. Postgress With SqlModel Orm - opensource databse

    4. Cloud Native Development Environment - docker - composse - dev container
        -  https://www.youtube.com/watch?v=eRbtrOIIP3k&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=4

    5. Kafka Event Driven Architecture - which help to decouple application and Emit (Produce) data in realtime. which All consumer can detect and act upon that in realtime.
        - https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/00_eda_challenge

    6. 


- [Code] (https://github.com/panaverse/learn-ge...)
- [Poetrry] (https://python-poetry.org/docs/)
- [Python Official Website] (https://www.python.org/)
- [FastAPI Official Website] (https://fastapi.tiangolo.com/learn/)
- [Docker Official Website] (https://docs.docker.com/)
- [Apache Kafka Documentation] (https://kafka.apache.org/20/documenta...)

# Learn Python

## Python Hello World
    
0. `First check python and poetry installed`
```

https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/09_create_project

docker version
poetry --version
```

1. `Create new project using. include name param to create code folder name else it will use project neme as default`



https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/10_microservice_helloworld

https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb

```
poetry new project_python --name src
```
2. `Add dependencies`
```
poetry add pytest httpx fastapi "uvicorn[standard]"
```
3. `Create main.py file in project_python/src first function that return string`
```
    def my_first_function()->str:
        return "Hello World";

    result: str = my_first_function();
    print(result);
```

4. `run project using`
```
poetry run python src/main.py
```
5. `create first unit test. each test should seperate in each file. file name and function should start with test`
```
from src import main

def test_my_first_function():
    r = main.my_first_function()
    assert r == "Hello World"


def test_my_first_function_2():
    r = main.my_first_function()
    assert r == "Hello World"
```
6. `run test`
```
poetry run pytest
```

7. `Create API using fastapi`
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

Now open browser:

    http://0.0.0.0:8000/

    http://0.0.0.0:8000/docs

    http://0.0.0.0:8000/openapi.json

8. `run server on http://127.0.0.1:8000/. .fastapi is filename. and :app is pastapi instance`
```
poetry run uvicorn src.fastapi:app --reload
```

9. `create fast api test test_fastapi.py`
```
from fastapi.testclient import TestClient

from project_python.fastapi import app

client = TestClient(app)

def test_root_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_items_path():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}
```
# Docker

https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/14_docker

## Now let's Containerize the app

make sure docker desktop is installed in your machine
some commands
```bash
docker images
docker image ls
docker ps
docker ps -a
docker build -f <filename> -t <Tag Name> .
docker run -d --name <container name> -p hostPort:containerPort #run container and ditacth
docker run -it --name <container name> -p hostPort:containerPort /bin/bash #run container and connect its bash. /bin/sh if bash bit found any default shell. 
dockers logs <contianer name>
docker exec -it dev-cont1 /bin/bash
exit
CTRL + P + Q //exit from container without closing the process
CTRL + C // break the process
CTRL + D // exit
``` 

10. `Convert this project setup in docker for that create dockerfile in root of your project with content below.`
    
```
# Use an official Python runtime as a parent image
FROM python:3.12

LABEL maintainer="anis-momin"

# Set the working directory in the container
WORKDIR /code

# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy the current directory contents into the container at /code
COPY . /code/

# Configuration to avoid creating virtual environments inside the Docker container
RUN poetry config virtualenvs.create false

# Install dependencies including development ones
RUN poetry install

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the app. CMD can be overridden when starting the container
CMD ["poetry", "run", "uvicorn", "src.fastapi:app", "--host", "0.0.0.0", "--reload"]
```

11. `Now create image using created dockerfile. -f is for use file. -t is name your image called tag your image. in the end dot is important. use current direcotry as code.`
```
docker build -f Dockerfile.dev -t py_poetry .
```

12. `Now run a container using created image`

Available oiptions -d detach mode. --name name the running container. -it interactive mode to accesss app using commandline. -p connect container and host port to access app from host machine
```
docker run -d --name first_app -p 8000:8000 py_poetry
```

13. `check log of running conrtainer`

```
docker logs first_app
```

14. `Now if want to run only test`
we can by pass provided command in Dockerfile. which only run when you start container.
for test purpouse we can use same configutation but just want to run test and close and remove cntainer
-it = interactive mode
--rm = once complete test remove container
-c = command. which will override privded command in dockerfile
```
docker run -it --rm py_poetry /bin/bash -c "poetry run pytest"
```

15. `running in production`

```
docker run -d -p 8000:8000 py_poetry_app
```

16. `create docker file using running container`

some time we debug running container and fix thing in that and its hard to remmeber what was the issue. so we can create new image of running container.

```
docker commit <running container ID> <new image name>
```

# Docker Compose

now we have dockerfile. each developer in a team can use this project but they can change configuration when they run project. like port mapping, names etc. 

so there is a way each one of there use same configutation , name port etc. in order to achieve this. we need to use docker composer. which installed by default with docker now.

now we ceate one project with docker file. now in microservice architecture we create multiple small appliaction. which interact with each other. so for that we will run multiple applicaation and run those using docker composer so 

create docker composer file. which is uses .yaml, .yml extension.
its like a json. but here we dont use brackets instead we use sapces to formate the hrearchy.

you can use 2 space, tabs etc.
     when line start with - means array item.

1. create new compose.yaml with content below.

```
version: "3.9"

name: cloudnative-ai-app

services:
  api:
    build:
      context: ./
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
```
2. now start with 

```
docker compose up -d
```
## Docker composer with multple app in it (used network and database)

3. Now add another container for database 
```
version: "3.9"

name: cloudnative-ai-app

services:
  api:
    build:
      context: ./
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    networks:
      - my-api-net
    depends_on:
      - postgres_db

  postgres_db:
    image: postgres:latest
    restart: always
    environment:
      - POSTGRES_USER=anismomin
      - POSTGRES_PASSWORD=12345
      - POSTGRES_DB=todos
    volumes:
      - postgres_db:/var/lib/postgresql/data
    ports:
      - "5433:5432"
    networks:
      - my-api-net
  
volumes:
  postgres_db:
    driver: local

networks:
  my-api-net:  # Define the custom network
```
2. now start with rebuild

```
docker compose up -d --build
```

# Dev Container
when you work with docker. if you change anything in code you always need to create new image in order to view that updated code.
But if you don't want to keep build new image while you are development/debug mode.

Overview
```https://www.youtube.com/watch?v=b1RavPr_878```

Use node modules with volumes in dev caonteiner to speed up build process
    ```https://www.youtube.com/watch?v=iDdJWIPRUx4```

Step 1: Install dev container extension in vscode
Step 2: Now open "Remote explorer" tab in vs code left bar.
Step 3: Now open "Remote explorer" tab in vs code left bar.
Step 2: if you already have running or stopped container of you existing code. it will 


# Kafka

### How kafaka process trillions of message.
https://www.youtube.com/watch?v=qVbAYHxW3xg&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=13

### Kafka hello world
https://www.youtube.com/watch?v=S4SXPSdTtUY&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=10

### Deep dive kafka Architecture
https://www.youtube.com/watch?v=uP38rnmUK40&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=11

https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/00_eda_challenge

# How To Learn Apache Kafka By Watching and Doing in 2024

[Kafka 101 Video Tutorial](https://developer.confluent.io/courses/apache-kafka/events/)

https://www.projectpro.io/article/learn-kafka/970

Upcoming Online Talks: Building Event-Driven Microservices with Apache Kafka

https://www.confluent.io/resources/online-talk/microservices-and-apache-kafka/


## Kafka 3.7 Docker Image

Follow this Quick Start with Docker and KRaft: 

https://kafka.apache.org/quickstart


**Using Kafka from Console with KRaft Using Docker Image**

Get the docker image

    docker pull apache/kafka:3.7.0

Start the kafka docker container

    docker run -p 9092:9092 apache/kafka:3.7.0

Open another console and check to see if container running:

    docker ps

Copy the container name, and give the following command to attach:

    docker exec -it <container-name> /bin/bash

Note: Kafka commands are in this directory in the container 

    /opt/kafka/bin

CREATE A TOPIC TO STORE YOUR EVENTS

Kafka is a distributed event streaming platform that lets you read, write, store, and process events (also called records or messages in the documentation) across many machines.

Example events are payment transactions, geolocation updates from mobile phones, shipping orders, sensor measurements from IoT devices or medical equipment, and much more. These events are organized and stored in topics. Very simplified, a topic is similar to a folder in a filesystem, and the events are the files in that folder.

So before you can write your first events, you must create a topic. Open another terminal session and run:

    /opt/kafka/bin/kafka-topics.sh --create --topic URA_EventStream --bootstrap-server localhost:9092


All of Kafka's command line tools have additional options: 

Note: run the kafka-topics.sh command without any arguments to display usage information. For example, it can also show you details such as the partition count of the new topic:

    /opt/kafka/bin/kafka-topics.sh --describe --topic URA_EventStream --bootstrap-server localhost:9092

Topic: URA_EventStream        TopicId: NPmZHyhbR9y00wMglMH2sg PartitionCount: 1       ReplicationFactor: 1	Configs:
    Topic: URA_EventStream Partition: 0    Leader: 0   Replicas: 0 Isr: 0


WRITE SOME EVENTS INTO THE TOPIC

A Kafka client communicates with the Kafka brokers via the network for writing (or reading) events. Once received, the brokers will store the events in a durable and fault-tolerant manner for as long as you need—even forever.

Run the console producer client to write a few events into your topic. By default, each line you enter will result in a separate event being written to the topic.

    /opt/kafka/bin/kafka-console-producer.sh --topic URA_EventStream --bootstrap-server localhost:9092

This is my first event

This is my second event

You can stop the producer client with Ctrl-C at any time.

READ THE EVENTS

Open another terminal session and run the console consumer client to read the events you just created:

    /opt/kafka/bin/kafka-console-consumer.sh --topic URA_EventStream --from-beginning --bootstrap-server localhost:9092

This is my first event

This is my second event

You can stop the consumer client with Ctrl-C at any time.

Feel free to experiment: for example, switch back to your producer terminal (previous step) to write additional events, and see how the events immediately show up in your consumer terminal.

Because events are durably stored in Kafka, they can be read as many times and by as many consumers as you want. You can easily verify this by opening yet another terminal session and re-running the previous command again.

# Kafka UI 

This is a popular open-source web UI specifically designed for viewing Kafka topics, messages, brokers, consumer groups, and even lets you create new topics. It's known for being lightweight, easy to set up, and supports secure connections. You can find the project on Github here:

https://github.com/provectus/kafka-ui

https://github.com/provectus/kafka-ui?tab=readme-ov-file#getting-started

    docker network create -d bridge kafka-net

    docker network ls

    docker run -p 9092:9092 --network kafka-net --name mykafka apache/kafka:3.7.0

    docker run -it -p 8080:8080 --network kafka-net -e DYNAMIC_CONFIG_ENABLED=true provectuslabs/kafka-ui

*Note: We will learn docker compose later, how to use docker compose to configure kafka, right now after a minutes it will go offline.

Then access the web UI at http://localhost:8080

Now Add cluster name
- mykafaka

Bootstrap server

- container host: kafkacon  (docker ps name coluumn)
- container port: 9092


In order to integrate kafka broker with kafkaUI use container name in the host

## Kafka with KRaft setup using Docker Compose | Kafka tutorial for beginners

https://www.youtube.com/watch?v=aTl2iSCynVc

https://medium.com/@tetianaokhotnik/setting-up-a-local-kafka-environment-in-kraft-mode-with-docker-compose-and-bitnami-image-enhanced-29a2dcabf2a9


# Kafka with Composer 
we need to run kafka with composer as above method just run few minutes and stop. due to security 

https://www.youtube.com/live/8nM1suLA0f4?si=_ruJF3xLO1tIu9l_&t=4817

https://github.com/panaverse/learn-generative-ai/tree/main/05_microservices_all_in_one_platform/15_event_driven/01_kafka_single_node_compose


# Authentication

https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/#scope

https://www.youtube.com/watch?v=8nM1suLA0f4&list=PL0vKVrkG4hWqWNAr6rcX0gOvU_eOULnJN&index=11

https://github.com/panaverse/learn-generative-ai/blob/main/05_microservices_all_in_one_platform/16_oauth2_auth/00_generate_access_token/README.md

```
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from jose import jwt, JWTError # type: ignore
from datetime import datetime, timedelta

ALGORITHM    = "HS256"
SECRET_KEY   = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

from fastapi.security import  OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

fake_users_db: dict[str, dict[str, str]] = {
    "anismomin": {
        "username": "anismomin",
        "full_name": "Anis Momin",
        "email": "anis@example.com",
        "password": "master123",
    },
    "hafeez": {
        "username": "hafeez",
        "full_name": "Hafeez Memon",
        "email": "hafeez@example.com",
        "password": "hafeezsecret",
    },
}

app = FastAPI(title="Authentication Service",
              version="0.0.1",
              servers=[
                  {
                      "url": "http://localhost:8001", #ADD NGROK URL HERE before creating GET Action
                      "description": "Development server"
                   }
              ])

def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    expire =  datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_access_token(token: str):
    decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decode_jwt

@app.get("/token")
def get_token(user_name: str):
    access_token = create_access_token(subject=user_name, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer", "user_name": user_name}

@app.get("/decode-token")
def decode_token(token: str):
    try:
        data = decode_access_token(token)
        return data
    except JWTError as e:
        return {"error" : str(e)}
    
@app.post("/login")
def login_request(data_form_user: Annotated[OAuth2PasswordRequestForm, Depends(OAuth2PasswordRequestForm)]):
    try:
        user_in_fake_db = fake_users_db.get(data_form_user.username)

        #Step 1 check user is exist
        if user_in_fake_db is None:
            raise HTTPException(status_code=400, detail="Incorrect username")

        #Step 2 check user password mactched
        if user_in_fake_db["password"] != data_form_user.password:
            raise HTTPException(status_code=400, detail="Incorrect password")

        access_token = create_access_token(data_form_user.username, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
        return {"access_token": access_token, "token_type": "bearer"}
    except JWTError as e:
        return {"error" : str(e)}
       

@app.get("/users")
def get_all_users(token: Annotated[str, Depends(oauth2_scheme)]):
    return fake_users_db
    
    
@app.get("/")
def index():
    return {"Hello": "Auth Service"}

```