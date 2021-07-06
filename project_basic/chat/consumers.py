# chat/consumers.py
# 소비자만들기
# HTTP 요청을 받아들이고 매핑된 URL로 이동, 이에 따라 views에 함수를 실행.
# 이와 유사하게 Channels 역시 WebSocket 연결을 받아들이면, root routing configuration 에서 소비자를 찾은 후에, 이벤트를 처리하기 위한 함수들을 호출

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
import json

class ChatConsumer(WebsocketConsumer):
    # websocket 연결 시 실행
    async def connect(self):
        # chat/routing.py 에 있는
        # url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
        # 에서 room_name 을 가져옵니다.
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.username = await self.get_name()

        # 그룹에 join
        # send 등 과 같은 동기적인 함수를 비동기적으로 사용하기 위해서는 async_to_sync 로 감싸줘야한다.
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # websocket 연결 
        await self.accept()
    
    @database_sync_to_async
    def get_name(self):
        return User.objects.all()[0].name

    async def disconnect(self, close_code):
        # 그릅에서 Leave
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # WebSocket 에게 메세지 receive    
    async def receive(self, text_date):
        text_data_json = json.loads(text_date)
        message = text_data_json['message']
            # 클라이언트로부터 받은 메세지를 다시 클라이언트로 보내준다.
        # room group 에게 메세지 send
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type' : 'chat_message',
                'message' : message
            }
        )
    
    # room group 에서 메세지 receive
    async def chat_message(self, event):
        message = event['message']

        # WebSocket 에게 메세지 전송
        await self.send(text_date=json.dumps({
            'message': message
        }))