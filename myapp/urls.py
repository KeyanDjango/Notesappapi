from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('api/crud',views.NoteViews.as_view(),name='notesapp')
]