from fastapi import APIRouter, Depends, Request

from app.services.jirawebhook import JiraWebhookService
#from schemas.foo import FooItem, FooItemCreate

from app.utils.service_result import handle_result

#from config.database import get_db

router = APIRouter()


@router.post("/v1/cisco/jirawebhook")
async def webhook_listener(request: Request):
    
    print('dentro de router.post()')
    result = await JiraWebhookService.listener(request)
    return handle_result(result)

