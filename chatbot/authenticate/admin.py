from django.contrib import admin
from .models import Organization, Agent, AgentCredentials, AgentEngine
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'created_at')
    search_fields = ['name']

@admin.register(AgentCredentials)
class AgentCredentialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_by', 'organization', 'expires_at', 'agent')
    search_fields = ['created_by__first_name', 'created_by__last_name', 'created_by__email', 'organization']
    raw_id_fields = ['organization']


@admin.register(AgentEngine)
class AgentEngineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'agent', 'owned_by')
    search_fields = ['name', 'slug']

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'documentation_url', 'name')
    search_fields = ['name']
