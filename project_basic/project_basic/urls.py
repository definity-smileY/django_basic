from django.contrib import admin
from django.urls import path, include
from testuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testuser/', include('testuser.urls')),
    path('', home),
    path('chat/', include('chat.urls')),
    path('polls/', include('polls.urls')),
]

# include() 함수는 다른 URLconf들을 참조할 수 있도록 도와줌.
# Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달합니다.

# 언제 include()를 사용해야 하나요?
# 다른 URL 패턴을 포함할 때마다 항상 include()를 사용해야 합니다. admin.site.urls가 유일한 예외입니다.

# path()함수에는 2개의 필수 인수인 route와 view 2개의 선택 가능한 인수로 kwargs와 name 까지 모두 4개의 인수가 전달 되었습니다.


"""
path() 인수: route
route 는 URL 패턴을 가진 문자열 입니다.  요청이 처리될 때, Django 는 urlpatterns 의 첫 번째 패턴부터 시작하여, 일치하는 패턴을 찾을 때 까지 요청된 URL 을 각 패턴과 리스트의 순서대로 비교합니다.

패턴들은 GET 이나 POST 의 매개 변수들, 혹은 도메인 이름을 검색하지 않습니다. 예를 들어, https://www.example.com/myapp/ 이 요청된 경우, URLconf 는 오직 myapp/ 부분만 바라 봅니다. https://www.example.com/myapp/?page=3, 같은 요청에도, URLconf 는 역시 myapp/ 부분만 신경씁니다.

path() 인수: view
Django 에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째 인수로 하고, 경로로 부터 〈캡처된〉 값을 키워드 인수로하여 특정한 view 함수를 호출합니다. 나중에 이에 대한 간단한 예제를 살펴보겠습니다.

path() 인수: kwargs
임의의 키워드 인수들은 목표한 view 에 사전형으로 전달됩니다. 그러나 이 튜토리얼에서는 사용하지 않을겁니다.

path() 인수: name
URL 에 이름을 지으면, 템플릿을 포함한 Django 어디에서나 명확하게 참조할 수 있습니다. 이 강력한 기능을 이용하여, 단 하나의 파일만 수정해도 project 내의 모든 URL 패턴을 바꿀 수 있도록 도와줍니다.

request 와 response 의 기본 흐름을 이해하셨다면, 튜토리얼 2장 에서 데이터베이스 작업을 시작해보세요.
"""