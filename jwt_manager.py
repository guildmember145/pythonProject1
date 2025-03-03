from typing import Coroutine
from fastapi import Request
from fastapi.security.http import HTTPAuthorizationCredentials
from jwt import encode, decode
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key="my_secret_key", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="my_secret_key", algorithms=['HS256'])
    return data



class JWTBearer(HTTPBearer):
   async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data ["email"] != "admin@gmail.com":
            raise HTTPException(status_code=200)