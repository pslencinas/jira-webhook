#from utils.app_exceptions import AppExceptionCase
from fastapi import FastAPI

from app.routers import jirawebhook
#from config.database import create_tables

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.utils.request_exceptions import (
    http_exception_handler,
    request_validation_exception_handler,
)
from app.utils.app_exceptions import app_exception_handler

#create_tables()

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, e):
    return await http_exception_handler(request, e)


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, e):
    return await request_validation_exception_handler(request, e)


app.include_router(jirawebhook.router)


@app.get("/")
async def root():
    print ("Hello world")
    return {"message": "Hello World"}
