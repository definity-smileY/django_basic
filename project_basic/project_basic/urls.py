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
