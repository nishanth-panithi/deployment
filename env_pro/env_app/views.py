from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import cloudtable
from .serializers import cloudtableserializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def welcome(req):
    return HttpResponse ('responce from deployment')
def sample(req):
    return JsonResponse({"msg":"jsonresponse from render"})
@csrf_exempt
def reg_user(req):
    user_data=json.loads(req.body)
    # ORM- oblect relational maping
    new_user=cloudtable.objects.create(id=user_data['id'],name=user_data['name'],email=user_data['email'],modile=user_data['mob'])
    return JsonResponse({'status':'user created sucessfully'})
