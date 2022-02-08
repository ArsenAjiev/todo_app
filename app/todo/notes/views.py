from django.shortcuts import render, redirect
from notes.models import Note
from notes.forms import AddNoteForm


def index(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            form = AddNoteForm()
            pass
    else:
        form = AddNoteForm()
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'notes': notes, 'form': form})



def delete_note(request, title_id):
    Note.objects.get(id=title_id).delete()
    return redirect('notes:index')
