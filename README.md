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


# Learn Python

## Python Hello World
    
0. `First check python and poetry installed`
```
docker version
poetry --version
```

1. `Create new project using. include name param to create code folder name else it will use project neme as default`

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