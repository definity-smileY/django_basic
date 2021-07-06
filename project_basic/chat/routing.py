# 소비자 라우팅을 처리하기 위해서 앱 안에 routing 추가
from django.conf.urls import url
from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer),
]
# 이 라우팅 파일을 장고가 인식할 수 있도록 프로젝트디렉토리에 있는 라우팅에 추가