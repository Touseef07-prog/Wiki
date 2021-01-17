from django.urls import path

from . import views

urlpatterns = [
    path("search", views.search, name="search"),
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.show_entry, name="show_entry"),
    path("page", views.new_page, name="page"),
    path("create_page", views.create_page, name="create_page"),
    path("editing", views.editing, name="editing"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("random",views.Random,name="random")


]
