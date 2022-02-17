from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm


@login_required
def index_view(request):
    items = Note.objects.filter(user=request.user)
    return render(request, 'notes/index.html', {'items': items})


@login_required
def save_form_view(request, note_pk=None):
    instance = Note(user=request.user)
    form = NoteForm()

    if note_pk:
        instance = get_object_or_404(Note, user=request.user, pk=note_pk)
        form = NoteForm(instance=instance)

    if request.method == 'POST':
        form = NoteForm(instance=instance, data=request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('notes:update', instance.pk)

    return render(request, 'notes/form.html', {'form': form, 'note_pk': note_pk})


@login_required
def destroy_view(request, note_pk):
    note = get_object_or_404(Note, id=note_pk, user=request.user)
    note.delete()
    return redirect('notes:index')
