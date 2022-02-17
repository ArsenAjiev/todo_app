from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('add/', views.save_form_view, name='create'),
    path('edit/<int:note_pk>/', views.save_form_view, name='update'),
    path('del/<int:note_pk>/', views.destroy_view, name='destroy'),
]
