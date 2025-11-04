from django.urls import path
from .import views

urlpatterns = [
    path("", views.sticky_note_display, name="sticky_note_display"),
    path("sticky_note/new/", views.sticky_note_create, name="sticky_note_create"),
    path("sticky_note/<int:pk>/edit/", views.sticky_note_update, name="sticky_note_update"),
    path("sticky_note/<int:pk>/delete/", views.sticky_note_delete, name="sticky_note_delete"),
]