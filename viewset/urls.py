from django.urls import path
from . import views

urlpatterns = [
    path("<int:set_id>/", views.view_set),
]