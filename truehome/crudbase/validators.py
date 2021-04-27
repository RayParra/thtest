from django.forms import ValidationError
from datetime import datetime

class CheckDate:
    def __init__(self, schedule):
        self.schedule = schedule
        
    def __call__(self, value):
        today = datetime.now()
        if value < today:
            raise ValidationError("No se puede crear actividad en fechas menores a la fecha actual.")
        return value