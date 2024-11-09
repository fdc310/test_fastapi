# from flask import request
import jwt
import datetime
from app.util.conf import redis_set
from starlette.requests import Request
import configparser

config = configparser.ConfigParser()


config_path = "config.ini"
config.read("", encoding="utf-8")

from typing import Optional
from fastapi import Header,HTTPException
secret = "dfx2ZynRrkI_f3-9KE4WVw"
'''
从缓存中获取用户id
'''


class TokenError(Exception):
    def __init__(self, message="An error occurred", code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message} - Code: {self.code}' if self.code else self.message



# def get_user_id():
#     token = Request.headers
#     user_id = redis_set.get(token)
#     if user_id:
#         return user_id.decode()
#     else:
#         raise TokenError()
async def get_user_id(Authorization: Optional[str] = Header):
    if Authorization is None:
        raise HTTPException(status_code=401,detail="验证不通过")
    try:
        print(Authorization)
        token = Authorization
        user_id = redis_set.get(token)
        return {"user_id": user_id}

    except:
        raise HTTPException(status_code=401,detail="验证不通过")





def Jwt_Token(user_id:int, user_name:str):
    # 定义负载
    payload = {
        'user_id': user_id,  # 示例用户ID
        'user_name': user_name,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24 * 30)  # 设置过期时间为30t天
    }

    # 定义秘钥
    # secret = config.get('OPTION', 'Secret_key')


    # 生成JWT
    token = jwt.encode(payload, secret, algorithm='HS256')

    return token


async def get_id(Authorization: Optional[str] = Header):
    if Authorization is None:
        raise HTTPException(status_code=401,detail="验证不通过")
    try:
        token = Authorization
        # 解码JWT
        # secret = config.get('CONFIGS', 'Secret_key')
        decoded_payload = jwt.decode(token, secret, algorithms=['HS256'])
        print(type(decoded_payload.get('user_id')))
        return decoded_payload.get('user_id')
    except jwt.ExpiredSignatureError as e:
        # 处理过期令牌的情况
        print("The token has expired.")
        return e
    except jwt.InvalidTokenError as e:
        # 处理无效令牌的情况
        print("Invalid token.")
        return e
