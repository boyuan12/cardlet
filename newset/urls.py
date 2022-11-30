from django.urls import path
from . import views

urlpatterns = [
    path("", views.new_set),
    path("upload/", views.upload_set_via_csv),
]