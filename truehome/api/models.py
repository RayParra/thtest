from django.db import models

# Create your models here.

class Property(models.Model):
    title = models.CharField(max_length=255, null=False)
    address = models.TextField(null=False)
    description = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
    disable_at = models.DateTimeField(auto_now=True, null=True)
    status = models.CharField(max_length=35, null=False)
    
    def __str__(self):
        return self.title



class Survey(models.Model):
    answers = models.JSONField(default={}, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    


class Activity(models.Model):
    property_id =  models.ForeignKey(Property, on_delete=models.CASCADE)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
    schedule = models.DateTimeField(auto_now=False, null=False)
    title = models.CharField (max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    update_at = models.DateTimeField(auto_now=True, null=False)
    status = models.CharField(max_length=35, null=False)
    
    
    def __str__(self):
        return self.title
