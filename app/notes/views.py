from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm


@login_required
def index_view(request):
    items = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {'items': items})


@login_required
def create_view(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            form.save()
            return redirect('notes:index')
    return render(request, 'notes/form.html', {'form': form})


@login_required
def destroy_view(request, pk):
    note = get_object_or_404(Note, id=pk, user=request.user)
    note.delete()
    return redirect('notes:index')
