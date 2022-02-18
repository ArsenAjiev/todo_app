from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from todos.models import Todo
from todos.forms import TodoForm


# Create your views here.
@login_required
def index_view(request):
    form = TodoForm()
    items = Todo.objects.filter(user=request.user)
    return render(request, 'todos/index.html', {'items': items, 'form': form})


@login_required
def destroy_view(request, note_pk):
    item = get_object_or_404(Todo, id=note_pk, user=request.user)
    item.delete()
    return redirect('todos:index')
