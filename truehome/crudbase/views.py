from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from datetime import datetime, timedelta

from api.models import Activity
from .forms import CreateActivityForm
# Create your views here.

class CreateActivityView(generic.CreateView):
    template_name = "crudbase/create_activity.html"
    model = Activity
    form_class = CreateActivityForm
    success_url = reverse_lazy("crudbase:list")



class ListActivityView(generic.ListView):
    template_name = "crudbase/list.html"
    model = Activity
    
    def get_queryset(self):
        today = datetime.now()
        lessdays = timedelta(days=3)
        moredays = timedelta(days=14)
        lfilter = today - lessdays
        rfilter = today + moredays
        return Activity.objects.filter(schedule__gt=lfilter, schedule__lt=rfilter)
    