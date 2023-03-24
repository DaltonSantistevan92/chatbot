import re
# from django.utils import timezone
from breathecode.authenticate.models import AgentCredentials
from .models import DecisionTemplate, Option
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI, OpenAIChat

# def ask_which_option():
def generate_text(text, credentials, model_slug):
    openai_chat_list = ['gpt-3.5-turbo']
    if model_slug in openai_chat_list:
        llm = OpenAIChat(model_name=model_slug , n=2, openai_api_key=credentials)
        
    else:
        llm = OpenAI(model_name=model_slug , n=2, best_of=2, openai_api_key=credentials)
    answer = llm(text)
    return  answer


def complete(decision_template_id):
    decision = DecisionTemplate.objects.filter(id=decision_template_id).first()
    job.started_at = timezone.now()
    agent = job.template.engine.agent
    credentials = AgentCredentials.objects.filter(organization__id=org_id, agent=agent).first()

    if job.template is not None:
        variables = list(job.template.variables.keys())
        for var in variables:
            if var not in job.inputs:
                job.status = ERROR
                raise ValueError(f'Missing key {var} inside inputs dictionary')
        def replace_variables(text, variables_object):
            for key, value in variables_object.items():
                text = text.replace('{' + key + ':' + value + '}', '{' + key + '}').replace('{' + key + ': ' + value + '}', '{' + key + '}').replace('{ ' + key + ': ' + value + ' }', '{' + key + '}').replace('{ ' + key + ':' + value + ' }', '{' + key + '}').replace('{' + key + ':' + value + ' }', '{' + key + '}')
                # I'm trying to manage some possibilities that someone can typically write the variables in the template
                text = text.replace(',', '')
            return text
        text = replace_variables(job.template.body, job.template.variables)
        prompt = PromptTemplate(
            input_variables=variables,
            template=text,
        )
        response = prompt.format(**job.inputs)
        job.prompt = response
        model_slug = job.template.engine.slugify()
        job.answer = generate_text(response, credentials.token, model_slug)
        job.status = SUCCESS
        job.ended_at = timezone.now()
        job.save()
        return job
    job.answer = generate_text(job.prompt, credentials.token)
    job.status = SUCCESS
    job.ended_at = timezone.now()
    job.save()
    return job
    