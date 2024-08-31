from datetime import timedelta

ALGORITHM    = "HS256"
SECRET_KEY   = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    expire =  datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def decode_access_token(token: str):
    decode_jwt = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return decode_jwt