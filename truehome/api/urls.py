from django.urls import path
from api import views


app_name = "api"


urlpatterns = [
     path('v1/list_activity/', views.activity_list_api_view, name="activity_list_def"),
     path('v1/detail_activity/<int:pk>', views.activity_detail_api_view, name="activity_detail_def"),
     
     path('v2/list_survey/', views.SurveyListAPIView.as_view(), name="survey_list"),
     path('v2/detail_survey/<int:pk>', views.SurveyDetailAPIView.as_view(), name="survey_detail"),
     path('v2/list_property/', views.PropertyListAPIView.as_view(), name="property_list"),
     path('v2/detail_property/<int:pk>', views.PropertyDetailAPIView.as_view(), name="property_detail"),
     path('v2/list_activity/', views.ActivityListAPIView.as_view(), name="activity_list"),
     path('v2/detail_activity/<int:pk>', views.ActivityDetailAPIView.as_view(), name="activity_detail"),
     
     path('v3/create_activity/', views.ActivityCreateAPIView.as_view(), name="activity_create"),
]
