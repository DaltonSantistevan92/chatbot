from django.contrib import admin
from .models import Option, DecisionTemplate, DecisionJob
# Register your models here.


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','link', 'organization', 'created_at')
    search_fields = ['name']


@admin.register(DecisionTemplate)
class DecisionTemplateAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'organization','body', 'created_at')
    list_filter = ['organization']

@admin.register(DecisionJob)
class DecisionJobAdmin(admin.ModelAdmin):

    list_display = ('id', 'status','user_input', 'started_at', 'ended_at')
    list_filter = ['status']
