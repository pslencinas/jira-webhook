from fastapi import Request
from webexteamssdk import WebexTeamsAPI
import json

from app.utils.service_result import ServiceResult

access_token = 'YTNmNjFlYTYtNDAyOS00NTM3LWFjMDMtM2YxMDhhNGYxZWZkNmExMzJkNjgtNmIy_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
WEBEX_BOT_USERNAME = 'githubissues@webex.bot' 


class GithubbotService():
    async def listener(request: Request) -> ServiceResult:

        print("\ndentro GithubotService().listener\n")
        api = WebexTeamsAPI(access_token = access_token)

        #print("\ndentro del POST webexBot v1/tlogic/vista/parte_diario")
        
        headers = request.headers
        body = await request.json()
        print(type(body))
        #body = json.dumps(body)
        print('\nwebexBot :: HEADER >> {}'.format(headers))
        print('\nwebexBot :: BODY >> {}'.format(body))
        
        message = 'OK'

        if body.get("resource", None) == 'messages' and body.get("name", None) == 'Cisco GitHub Bot':

            data_id = body["data"]["id"]
            room_id = body["data"]["roomId"]

            personalEmail = body["data"]["personEmail"]
            print('\n:::::::::::::: Dentro del Menu Bienvenida: {}\n'.format(personalEmail))

            if personalEmail == WEBEX_BOT_USERNAME:
                message = api.messages.get(data_id)
                print('Mensaje: '+ message.text)
                message = 'OK'

                #response = json.dumps({'message': message})
                #return response, 200

            else:
                msg = """
                    Hi {}. Welcome to GitHub Bot Issues
                    """.format(personalEmail)

                api.messages.create(room_id, markdown="{}".format(msg))

                #message = 'OK'

        elif body.get('issue', None):
            repository_url = body['issue']['repository_url']
            action = body['action']
            title = body['issue']['title']
            state = body['issue']['state']

            msg = """
                    GitHub Bot Issue Tracker
                    Title: {}
                    Action: {}
                    State: {}
                    Repository URL: {}
                    
                    """.format(title, action, state, repository_url)

            api.messages.create(toPersonEmail='plencina@cisco.com', markdown="{}".format(msg))

                
        return ServiceResult(message)
