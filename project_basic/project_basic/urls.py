from django.contrib import admin
from django.urls import path, include
from testuser.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testuser/', include('testuser.urls')),
    path('', home),
    path('chat/', include('chat.urls')),

]
