from django.shortcuts import render
from django.views import generic

from datetime import datetime
import requests

# Create your views here.


class ListActivityClient(generic.TemplateView):
    template_name = "client_test/list_activity_client.html"
    
    def get(self, request):
        url ="http://localhost:8000/api/v2/list_activity/" #"http://localhost:8000/api/v3/activities/"
        response = requests.get(url)
        object_activities = response.json()
        dt_act = []
        date = response.json()[0]["schedule"]
        d = date[:4] + ',' + date[5:7] + ',' + date[8:10] + ',' + date[11:13] + ',' + date[14:16]
        print(d)
        print(type(date))
        for item in object_activities:
            dt_act.append(item["schedule"])
            date = item["schedule"]
            d = date[:4] + ',' + date[5:7] + ',' + date[8:10] + ',' + date[11:13] + ',' + date[14:16]
            
        ctx = {
            'object_list': response.json()
        }
        return render(request, "client_test/list_activity_client.html", ctx)