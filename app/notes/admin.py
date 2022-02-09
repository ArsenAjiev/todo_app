from django.contrib import admin
from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    fields = ('title', 'text', 'user')
    readonly_fields = ('created_at',)
    search_fields = ('text',)
