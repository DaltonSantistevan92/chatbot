from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Organization(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    documentation_url = models.URLField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.name

class AgentCredentials(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)
    token = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    expires_at = models.DateTimeField(default=None, blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


class AgentEngine(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=250, help_text='This has to be the name used by the agent to identify the engine')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    owned_by = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def slugify(self):
        return self.slug
        
    def __str__(self):
        return self.name