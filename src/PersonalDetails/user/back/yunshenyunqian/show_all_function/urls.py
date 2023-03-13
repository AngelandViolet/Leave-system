from django.urls import path
from . import views

urlpatterns = [
    path('all_data', views.show_all_data),
    path('change_data', views.show_change_data),
    path('cancel_change', views.cancel_change),
    path('cancel_leave', views.cancel_leave),
]