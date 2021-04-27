from django import forms

from api.models import Activity

class CreateActivityForm(forms.ModelForm):
    schedule = forms.DateTimeField(required=False, widget=forms.TextInput(attrs={"type": "date"}))
    #property_id = forms.ChoiceField(choices=[(property_id.id, choice) for choice in Activity.objects.filter(status="active")])
    property_id = forms.ModelChoiceField(queryset=Activity.objects.filter(status="active"))
    class Meta:
        model = Activity
        fields = ("schedule", "title", "status", "property_id", "survey_id")
        