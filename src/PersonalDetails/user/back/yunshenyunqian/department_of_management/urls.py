from django.urls import path
from . import views
urlpatterns = [
    path('manager_log', views.manager_log),
]
