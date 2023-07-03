from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
# CRUDとDjangoのテンプレート

# 読み込む【情報をとる】データの一覧をリストとして表示すること
class TodoList(ListView):
    template_name = 'list.html' # どのHTMLを使用するかを記載
    model = TodoModel # どのテーブルを使用するかを記載

# 読み込む【情報をとる】データの中身を表示
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

# 作成する
class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate') # 作成formに表示させるfieldを記載
    success_url = reverse_lazy('list') # データが正常に作成された時に遷移させる先。「'list'」はurls.pyに記載したnameを呼び出す。

# 削除する
class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

# 更新する
class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')
