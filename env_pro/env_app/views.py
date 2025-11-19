from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import cloudtable
from .serializers import cloudtableserializer
from django.views.decorators.csrf import csrf_exempt
import cloudinary
# Create your views here.

def welcome(req):
    return HttpResponse ('responce from deployment')
def sample(req):
    return JsonResponse({"msg":"jsonresponse from render"})
@csrf_exempt
# def reg_user(req):
#     user_data=json.loads(req.body)
#     # ORM- oblect relational maping
#     new_user=cloudtable.objects.create(id=user_data['id'],name=user_data['name'],email=user_data['email'],mobile=user_data['mob'])
#     return JsonResponse({'status':'user created sucessfully'})

def reg_user(req):
    if req.method =='POST':
        try:
            sid=req.POST.get('id')
            sname=req.POST.get('name')
            semail=req.POST.get('email')
            smobile=req.POST.get('mobile')
            sphoto=req.FILES.get('photo')

            img_url=cloudinary.uploader.upload(sphoto)

            print(img_url['secure_url'])
     
            new_user=cloudtable.objects.create(id=sid,
                                               name=sname,
                                               email=semail,
                                               mobile=smobile,
                                               photo=img_url['secure_url'])

            return JsonResponse({'status':'user created sucessfully','detsils':list(new_user.values())})
        except Exception as e :
            return JsonResponse({"error":str(e)},status=400)
    return JsonResponse({"error":"Only POST method allowed"},status=405)


