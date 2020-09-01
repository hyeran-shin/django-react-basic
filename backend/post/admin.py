from django.contrib import admin

# Register your models here.

from .models import Post
admin.site.register(Post) #admin에 해당 모델 등록, post 객체 만들기
