# Python Hello World
1. `Create new project using`
```
poetry new project_python
```
2. `Add dependencies`
```
poetry add pytest requests fastapi "uvicorn[standard]"
```
3. `Create main.py file in project_python/project_python first function that return string`
```
    def my_first_function()->str:
        return "Hello World";

    result: str = my_first_function();
    print(result);
```

4. `run project using`
```
poetry run python project_python/main.py
```
5. `create first unit test. each test should seperate in each file. file name and function should start with test`
```
from project_python import main

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
