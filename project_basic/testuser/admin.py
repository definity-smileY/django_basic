from django.contrib import admin
from .models import testuser
# Register your models here.
class TestuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(testuser, TestuserAdmin)