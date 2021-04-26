from django.shortcuts import render
from django.views import generic

import requests
# Create your views here.


class ListActivityClient(generic.TemplateView):
    template_name = "client_test/list_activity_client.html"
    
    def get(self, request):
        url = "http://localhost:8000/api/v1/list_activity/"
        response = requests.get(url)
        ctx = {
            'object_list': response.json()
        }
        return render(request, "client_test/list_activity_client.html", ctx)