from django.shortcuts import render, HttpResponse
from .models import Job
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def create_job(request):
    try:
        req_dict = json.loads(json.dumps(request.POST))
        job_obj = Job.objects.create(**req_dict)
        return HttpResponse("Job created Successfully")
    except Exception as e:
        return HttpResponse(str(e))


