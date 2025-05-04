from django.urls import include,path
from . import views


urlpatterns = [
    path('',views.jobs_list,name="Jobs"),
    path('<int:id>',views.job_details,name="Job_details")
]
