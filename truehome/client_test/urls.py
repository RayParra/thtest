from django.urls import path
from client_test import views

app_name = "client_test"

urlpatterns = [
    path('list_activity_client/', views.ListActivityClient.as_view(), name="list_activity_client"),
]
