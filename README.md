# Learn Python

## Python Hello World
    
0. `First check python and poetry installed`
```
docker version
poetry --version
```

1. `Create new project using. include name param to create code folder name else it will use project neme as default`
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

## Dev Container
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