from django.shortcuts import render, HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def create_user(request):
    try:
        req_dict = json.loads(json.dumps(request.POST))
        job_obj = User.objects.create(**req_dict)
        return HttpResponse("User created Successfully")
    except Exception as e:
        return HttpResponse(str(e))



