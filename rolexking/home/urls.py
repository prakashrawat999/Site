from django.contrib import admin
from django.urls import path, re_path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    re_path(r"^.*$", views.custom_page_not_found, name="custom_page_not_found"),
]
