from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
def upload_image(instance, file_name):
    img_name ,extension = file_name.split(".")
    return f"jobs/{instance.id}.{extension}"

class Job(models.Model):
    title = models.CharField(max_length=200)
    # localtion
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default= 1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', verbose_name="Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_image)
    
    def __str__(self):
        return self.title
    

