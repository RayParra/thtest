from django.contrib import admin

# Register your models here.

from .models import Property, Activity, Survey


@admin.register(Property)
class AdminProperty(admin.ModelAdmin):
    list_display = ["title", "created_at", "status"]
    

@admin.register(Activity)
class AdminActivity(admin.ModelAdmin):
    list_display = ["title", "property_id", "schedule", "created_at", "status"]


@admin.register(Survey)
class AdminSurvey(admin.ModelAdmin):
    list_display = ["answers", "created_at"]