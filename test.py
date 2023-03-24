from chatbot.chat.models import DecisionJob
from chatbot.authenticate.models import AgentCredentials

def complete(decision_template_id):
    decision = DecisionJob.objects.filter(id=decision_template_id).first()
    # decision.started_at = timezone.now()
    agent = decision.template.engine.agent
    organization = decision.template.organization
    credentials = AgentCredentials.objects.filter(organization=organization, agent=agent).first()


    def generate_option_text(decision_template):
        options = decision_template.option_set.all()
        option_text = ""
        for option in options:
            option_text += f"{option.name}:{option.body},url:{option.link},"
        return option_text[:-1]
    
    options_text = generate_option_text(decision.template)
    text = decision.template.body + options_text
    print(text)

    # decision.prompt = text
    # model_slug = job.template.engine.slugify()
    # job.answer = generate_text(response, credentials.token, model_slug)
    # job.status = SUCCESS
    # job.ended_at = timezone.now()
    # job.save()
    # return job
    

complete(1)