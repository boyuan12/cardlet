from django.urls import path
from . import views

urlpatterns = [
    path("<int:set_id>/", views.view_set),
    path("json/<int:set_id>/", views.view_set_json),
    path("<int:set_id>/learn/", views.learn),
]