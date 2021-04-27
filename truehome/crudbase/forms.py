from django import forms
from django.forms import ValidationError
from django.utils import timezone
from .validators import CheckDate
from api.models import Activity

class CreateActivityForm(forms.ModelForm):
    schedule = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={"type": "date"}))
    #property_id = forms.ChoiceField(choices=[(property_id.id, choice) for choice in Activity.objects.filter(status="active")])
    #property_id = forms.ModelChoiceField(queryset=Activity.objects.filter(status="active"))
    
    def clean_schedule(self):
        schedule = self.cleaned_data["schedule"]
        today = timezone.now()
        
        if schedule < today:
            raise ValidationError("No se puede agendar Actividad con fecha menor a la fecha actual")
        return schedule
    
    class Meta:
        model = Activity
        fields = ("schedule", "title", "status", "property_id", "survey_id")
    
