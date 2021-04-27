from rest_framework import serializers
from .models import Property, Survey, Activity
from django.utils import timezone
from datetime import datetime, timedelta
 
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model= Property
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
        
# Read Activity full data
class ActivitySerializerRead(serializers.ModelSerializer):
    property_id = PropertySerializer()
    survey_id = SurveySerializer()
    schedule = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'


# Create Activity, validation date and time
class ActivitySerializer(serializers.ModelSerializer):    
    class Meta:
        model = Activity
        fields = '__all__'
    
    def validate_schedule(self, value):
        today = datetime.now()
       
        date = datetime(value.year, value.month, value.day, value.hour)
        date2 = datetime(today.year, today.month, today.day, today.hour)
     
        if (date < date2) or date.hour == date2.hour:
            raise serializers.ValidationError("Hora o Fecha invalida: Las fechas no pueden ser anterior a la actual o la hora no puede ser igual")
        return value
    