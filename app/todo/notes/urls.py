from django.urls import path
from notes.views import index, delete_note


app_name = 'notes'

urlpatterns = [
    path('', index, name='index'),
    path('delete/<title_id>/', delete_note, name='delete_note'),
]





