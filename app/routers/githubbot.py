from fastapi import APIRouter, Depends, Request

from app.services.githubbot import GithubbotService
#from schemas.foo import FooItem, FooItemCreate

from app.utils.service_result import handle_result

#from config.database import get_db

router = APIRouter()


@router.post("/v1/cisco/githubbot")
async def webhook_listener(request: Request):
    
    print('dentro de router.post()')
    result = await GithubbotService.listener(request)
    return handle_result(result)

