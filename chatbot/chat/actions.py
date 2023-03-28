import re
# from django.utils import timezone
from chatbot.authenticate.models import AgentCredentials
from .models import DecisionTemplate, Option, DecisionJob
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory


def complete(decision_template_id, input_text):
    decision = DecisionJob.objects.filter(id=decision_template_id).first()
    agent = decision.template.engine.agent
    organization = decision.template.organization
    credentials = AgentCredentials.objects.filter(organization=organization, agent=agent).first()


    def generate_option_text(decision_template):
        options = decision_template.option_set.all()
        option_text = ""
        for option in options:
            option_text += f"{option.name}:{option.body},url:{option.link} |"
        return option_text[:-1]
    
    options_text = generate_option_text(decision.template)
    
    template = """Eres un chatbot asistente de la empresa XtrimTV, vas a recibir el input de un cliente de la empresa, salúdalo y dale las indicaciones correctas según su requerimiento.
    Vas a tener una lista de opciones a tu disposición, cada una de las cuales puede ser la que el cliente quiere realizar.
    Tu objetivo es darle un mensaje apropiado según la opción que quiere realizar y devolverle, además del mensaje, el url para realizar el trámite en caso de que el trámite esté contemplado en las opciones

    Devuelve en el siguiente formato:

    Debes redactar un mensaje apropiado para el usuario y darle el link de la opción que desea realizar dentro de un string con forma de HTML
    Por ejemplo: <div>¡Hola! Para ver los términos y condiciones ver a siguiente enlace <a href="url a los TyC"> Términos y condiciones </a> </div>

    Input del usuario: {human_input}

    {history}
    
    Las opciones son:

    """

    final_template = template + options_text
    prompt = PromptTemplate(
        input_variables=["history", "human_input"], 
        template=final_template
    )


    chatgpt_chain = LLMChain(
        llm=ChatOpenAI(temperature=0, openai_api_key=credentials.token), 
        prompt=prompt, 
        memory=ConversationBufferWindowMemory(k=2),
    )
    output = chatgpt_chain.predict(human_input=input_text)
    # print(output)
    return output


































# def generate_text(text, credentials, model_slug):
#     chat = ChatOpenAI(temperature=0, openai_api_key=credentials)

#     messages = [
#     SystemMessage(content="You are a helpful assistant that translates English to French."),
#     HumanMessage(content="Translate this sentence from English to French. I love programming.")
#     ]
#     answer = llm(text)
#     return  answer


# def complete(decision_template_id):
#     decision = DecisionJob.objects.filter(id=decision_template_id).first()
#     decision.started_at = timezone.now()
    # agent = decision.template.engine.agent
    # organization = decision.template.organization
    # credentials = AgentCredentials.objects.filter(organization=organization, agent=agent).first()


    # def generate_option_text(decision_template):
    #     options = decision_template.option_set.all()
    #     option_text = ""
    #     for option in options:
    #         option_text += f"{option.name}:{option.body},url:{option.link},"
    #     return option_text[:-1]
    
    # options_text = generate_option_text(decision.template)

#     text = decision.template.body + options_text
#     chat = ChatOpenAI(temperature=0, openai_api_key=credentials)

#     messages = [
#     SystemMessage(content=text),
#     HumanMessage(content=decision.user_input)
#     ]

#     # chat(messages)

#     print(chat.messages)
#     # job.status = SUCCESS
#     # job.ended_at = timezone.now()
#     # job.save()
#     # return job
    
