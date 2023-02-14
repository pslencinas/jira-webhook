from fastapi import Request
from webexteamssdk import WebexTeamsAPI
import json

from app.utils.service_result import ServiceResult

class JiraWebhookService():
    async def listener(request: Request) -> ServiceResult:

        print("\ndentro JiraWebhookService().listener\n")
        
        #print("\ndentro del POST webexBot v1/tlogic/vista/parte_diario")
        
        headers = request.headers
        body = await request.json()
        print(type(body))
        #body = json.dumps(body)
        print('\nwebexBot :: HEADER >> {}'.format(headers))
        print('\nwebexBot :: BODY >> {}'.format(body))
        
        message = 'OK'

                
        return ServiceResult(message)
