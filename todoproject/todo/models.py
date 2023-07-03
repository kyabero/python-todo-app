from django.db import models

# Create your models here.

# 選択したものによって色を変える
CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model): # 以下にフィールドを定義していく
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE # 選択肢の中から選択できるようなる
        )
    duedate = models.DateField() # 日付を表示
    
    # オブジェクトが作成された時に実行される関数。管理画面のオブジェクトタイトルを表示。
    def __str__(self):
        return self.title
