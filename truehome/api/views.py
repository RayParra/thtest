#from django.shortcuts import render
#from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django.shortcuts import get_object_or_404

from .models import Activity, Property, Survey
from .serializers import ActivitySerializer, ActivitySerializerRead, PropertySerializer, SurveySerializer

# Create your views here.

##### generics.CreateAPIView #####
### v3/activity_create ### Write Only
class ActivityCreateAPIView(generics.CreateAPIView):
    serializer_class = ActivitySerializer

### v3/activities ### List and Write
class ActivityListCreateView(generics.ListCreateAPIView):
    serializer_class = ActivitySerializer
    queryset = ActivitySerializer.Meta.model.objects.all()


##### APIView #####

class SurveyListAPIView(APIView):
    def get(self, request):
        survey_data = Survey.objects.all()
        data = SurveySerializer(survey_data, many=True).data
        return Response(data)


class SurveyDetailAPIView(APIView):
    def get(self, request, pk):
        survey_data = get_object_or_404(Survey, pk=pk)
        data = SurveySerializer(survey_data).data
        return Response(data)
    


class PropertyListAPIView(APIView):
    def get(self, request):
        property_data = Property.objects.all()
        data = PropertySerializer(property_data, many=True).data
        return Response(data)
    
    
class PropertyDetailAPIView(APIView):
    def get(self, request, pk):
        property_data = get_object_or_404(Property, pk=pk)
        data = PropertySerializer(property_data).data
        return Response(data)


### v2/activity_list ### Read Only
class ActivityListAPIView(APIView):
    def get(self, request):
        activity_data = Activity.objects.all()
        data = ActivitySerializerRead(activity_data, many=True).data
        return Response(data)
    

### v2/activity_detail ### Read Only
class ActivityDetailAPIView(APIView):
    def get(self, request, pk):
        activity_data = get_object_or_404(Activity, pk=pk)
        data = ActivitySerializer(activity_data).data
        return Response(data)
        


##### @API_VIEW #####

@api_view(["GET", "POST"])
def activity_list_api_view(request):
    # List v1/activity_list # Read only
    if request.method == "GET":
        activity_data =  Activity.objects.all()
        data = ActivitySerializerRead(activity_data, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    # Create v1/activity_list # Write only
    elif request.method == "POST":
        data = ActivitySerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(["GET", "PUT", "DELETE"])
def activity_detail_api_view(request, pk=None):
    # Detail v1/activity_detail # Read only
    activity_data = Activity.objects.filter(id=pk).first()
    if activity_data:
        if request.method=='GET':
            data = ActivitySerializer(activity_data).data
            return Response(data, status=status.HTTP_200_OK)
        # Update v1/activity_update # Write only
        elif request.method=='PUT':
            data = ActivitySerializer(activity_data, data=request.data)
            if data.is_valid():
                data.save()
                return Response(data.data)
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        # Delete v1/activity_delete # write only
        elif request.method=='DELETE':
            activity_data.delete()
            return Response({"message": "Activity Removed Successfully"}, status=status.HTTP_200_OK)
    return Response({"message": "Activity Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        
    
    
# class ListActivityView(generic.ListView):
#     template_name = "api/list_activities.html"
#     model = Activity


# class NewActivityView(generic.CreateView):
#     template_name = "api/new_activity.html"
#     model = Activity
#     fields = "__all__"





 
 