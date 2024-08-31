from fastapi import FastAPI

app = FastAPI(title="Todo Service",
              version="0.0.1",
              servers=[
                  {
                      "url": "http://localhost:8000", #ADD NGROK URL HERE before creating GET Action
                      "description": "Todos Application server"
                   }
              ])

@app.get("/")
def index():
    return {"Hello": "Worldssadas"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}