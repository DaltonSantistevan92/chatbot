from django.db import models
from ..authenticate.models import Organization, AgentEngine
# Create your models here.
import re



class DecisionTemplate(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True, default=None)
    engine = models.ForeignKey(AgentEngine, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
        return self.name
    
    # def save(self, *args, **kwargs):
    #     from .actions import track_template_versions
    #     self.find_variables()
    #     self.variables = self.find_variables()
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    #     track_template_versions(self)


class Option(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    body = models.TextField()
    template = models.ForeignKey(DecisionTemplate, on_delete=models.CASCADE, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    link = models.URLField()
    def __str__(self):
        return self.name
    
PENDING = 'PENDING'
ERROR = 'ERROR'
SUCCESS = 'SUCCESS'
STATUS = (
    (PENDING, 'Pending'),
    (ERROR, 'Error'),
    (SUCCESS, 'Success'),
)

class DecisionJob(models.Model):

    status = models.CharField(max_length=9, choices=STATUS, default=PENDING)

    template = models.ForeignKey(DecisionTemplate, on_delete=models.CASCADE, null=True, blank=True)
    user_input = models.CharField(max_length=100)
    prompt = models.TextField(default=None, null=True, blank=True)
    answer = models.TextField(default=None, null=True, blank=True)
    
    started_at = models.DateTimeField( editable=True, blank=True, null=True)
    ended_at = models.DateTimeField(editable=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
