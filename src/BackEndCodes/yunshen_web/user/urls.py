from django.urls import path
from . import views

urlpatterns = [
    path('user_sign', views.user_sign),
    path('user_log', views.user_log),
    path('ask_leave', views.ask_leave),
    path('cancel_leave', views.cancel_leave),
    path('ask_change', views.ask_change),
    path('cancel_change', views.cancel_change),
    path('show_user_information', views.show_user_information),
    path('show_all_data', views.show_all_data),
    path('make_codes', views.make_codes),
]