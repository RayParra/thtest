from rest_framework import serializers
from .models import Property, Survey, Activity
import datetime
from datetime import timedelta
 
class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model= Property
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'
        

class ActivitySerializerRead(serializers.ModelSerializer):
    property_id = PropertySerializer()
    survey_id = SurveySerializer()
    schedule = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Activity
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = '__all__'
    
    def validate_schedule(self, value):
        today = datetime.datetime.now()
        #td = timedelta(days=-1)
       
        date = datetime.datetime(value.year, value.month, value.day)
        date2 = datetime.datetime(today.year, today.month, today.day)
     
        if date < date2:
            raise serializers.ValidationError("Fecha invalida: Las fechas no pueden ser anterior a la actual")
        return value
    