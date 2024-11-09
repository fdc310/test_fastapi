import json
from typing import List

from fastapi import APIRouter, Depends
from app.util.schemas import R



router = APIRouter(prefix="/home",tags=["home"])



@router.get("",summary="home")
async def home():
    return {"message":"成功了哈哈"}