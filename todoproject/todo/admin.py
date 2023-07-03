from django.contrib import admin
from .models import TodoModel

# Register your models here.

# 管理画面にどんな情報を表示するのかを記載。
admin.site.register(TodoModel)
