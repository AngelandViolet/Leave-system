from django.urls import path
from . import views
urlpatterns = [
    path('manager_log', views.manager_log),
    path('show_change_data', views.show_change_data),
    path('show_leave_data', views.show_leave_data),
    path('show_all_data', views.show_all_data),
]
