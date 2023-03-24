from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse('Hello World asd')



# class DecisionJob(generics.CreateAPIView):
#     queryset = CompletionJob.objects.all()
#     serializer_class = CompletionSerializer
#     permission_classes = [AllowAny]
#     def post(self, request, *args, **kwargs):
#         extension = request.data.get('extension')
#         token_key = request.data.get('token')
#         token=Token.objects.filter(key=token_key).first()
#         user = User.objects.filter(auth_token=token).first()
#         template_id = self.request.query_params.get('template_id')
#         template=PromptTemplate.objects.filter(id=template_id).first()
#         if template is None:
#             raise ValidationException('Template not found', code=404)
#         if extension:
#             inputs = self.request.data.get('inputs')
#         else:
#             inputs=dict(self.request.POST)
#             inputs.pop('organization')
#             inputs.pop('token')
#         for key, value in inputs.items():
#             inputs[key] = value
#         instance = CompletionJob.objects.create(template=template, inputs=inputs)
#         instance = complete(instance.id, template.organization.id)
#         data = {
#             'answer': instance.answer,
#             'completion': instance.id
#         }
#         return Response(data, status=status.HTTP_201_CREATED)

