from django.urls import path
from . import views
urlpatterns = [
    path('user_log', views.user_log),
    path('user_sign', views.user_sign)
]
