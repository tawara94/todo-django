from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Todo
from .forms import TodoForm
import logging

logger = logging.getLogger(__name__)


# 一覧表示
class TodoListView(View):
    template_name = 'todo/todo_list.html'

    def get(self, request):
        object_list = Todo.objects.all
        context = {'object_list': object_list}
        return render(request, self.template_name, context)


# 詳細表示
class TodoDetailView(View):
    template_name = 'todo/todo_detail.html'

    def get(self, request, pk):
        object = get_object_or_404(Todo, pk=pk)
        context = {'object': object}
        return render(request, self.template_name, context)


# 新規作成
class TodoCreateView(View):
    template_name = 'todo/todo_create.html'

    def get(self, request):
        form = TodoForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = TodoForm(request.POST)
        context = {'form': form}
        if not form.is_valid():
            return render(request, self.template_name, context)
        form.save()
        return redirect(reverse('todo:list'))


# 更新
class TodoUpdateView(View):
    template_name = 'todo/todo_update.html'

    def get(self, request, pk):
        object = get_object_or_404(Todo, pk=pk)
        form = TodoForm(instance=object)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        object = get_object_or_404(Todo, pk=pk)
        form = TodoForm(request.POST, instance=object)
        context = {'form': form}
        if not form.is_valid():
            return render(request, self.template_name, context)
        form.save()
        return redirect(reverse('todo:list'))


# 削除
class TodoDeleteView(View):
    template_name = 'todo/todo_confirm_delete.html'

    def get(self, request, pk):
        object = get_object_or_404(Todo, pk=pk)
        context = {'object': object}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        object = get_object_or_404(Todo, pk=pk)
        object.delete()
        return redirect(reverse('todo:list'))


class IndexView(View):
    def get(self, request):
        return redirect(reverse('todo:list'))
