from django.shortcuts import render,get_object_or_404
from .models import Job
# Create your views here.

def jobs_list(request):
    job_list = Job.objects.all()
    context = {
        'jobs':job_list
    }
    return render(request,"job/jobs_list.html", context)

def job_details(request, id):
    job_detail = get_object_or_404(Job,id=id)
    context = {
        'job':job_detail,
    }
    return render(request, 'job/job_details.html',context)