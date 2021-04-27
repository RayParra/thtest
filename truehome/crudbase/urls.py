from django.urls import path

from crudbase import views

app_name = "crudbase"

urlpatterns = [
    path('list/', views.ListActivityView.as_view(), name="list"),
    path('create_activity/', views.CreateActivityView.as_view(), name="create_activity"),
]
