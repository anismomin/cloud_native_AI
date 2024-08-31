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
