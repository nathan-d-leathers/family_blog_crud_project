from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("authors/", views.list_authors, name="list_authors"),
    path('authors/<int:author_id>/', views.list_entries, name="list_entries"),
    path('authors/<int:author_id>/entries/new/',
         views.add_entry, name="add_entry"),
    path('authors/<int:author_id>/entries/<int:entry_id>/',
         views.entry_info, name="entry_info"),
    path('authors/<int:author_id>/entries/<int:entry_id>/edit/',
         views.edit_entry, name="edit_entry"),
]
