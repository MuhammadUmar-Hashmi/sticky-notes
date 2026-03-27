from django.urls import path

from . import views

urlpatterns = [
    path("", views.note_list, name="note_list"),
    path("new/", views.note_create, name="note_create"),
    path("<int:id>/edit/", views.note_edit, name="note_edit"),
    path("<int:id>/delete/", views.note_delete, name="note_delete"),
    path("<int:id>/toggle-pin/", views.note_toggle_pin, name="note_toggle_pin"),
    path("<int:id>/set-color/", views.note_set_color, name="note_set_color"),
]

