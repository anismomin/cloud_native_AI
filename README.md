# Python Hello World
1. `Create new project using. include name param to create code folder name else it will use project neme as default`
```
poetry new project_python --name src
```
2. `Add dependencies`
```
poetry add pytest requests fastapi "uvicorn[standard]"
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