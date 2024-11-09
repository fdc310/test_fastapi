from fastapi import FastAPI, Depends
from starlette.responses import JSONResponse
from starlette.requests import Request
from loguru import logger  # 日志
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.middleware.cors import CORSMiddleware   # 中间键
from app.util.schemas import R
from app.api.router.admin import router as home
from app.api.router.audio_list import router as audio_list
from app.api.router.login import router as login
from app.api.router.chat import router as chat

app = FastAPI()


# 异常处理

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request,exc):
    return JSONResponse(content=R.fail(str(exc)).dict())


@app.exception_handler(HTTPException)
async def Http_exception(request,exc):
    return JSONResponse(content=R.fail(msg=exc.detail).dict())


# 中间件

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],  # 一个允许跨域请求的 HTTP 方法列表
    allow_headers = ["*"],  # 一个允许跨域请求的 HTTP 请求头列表
)


@app.middleware("http")
async def visit_log(request: Request ,call_next):
    logger.info(
        f"Client:{request.client} Method:{request.method}"
        f"Path:{request.url} Headers: {request.headers}"
    )
    # print(request.headers)
    reponse = await call_next(request)
    return reponse

app.include_router(home)
app.include_router(audio_list)
app.include_router(login)
app.include_router(chat)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("__main__:app", host="0.0.0.0", port=8026, reload=True)







