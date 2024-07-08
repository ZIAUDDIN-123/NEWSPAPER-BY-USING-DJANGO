from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Newspaper(models.Model):
    title=models.CharField(max_length=50)
    author_name=models.ForeignKey(User, on_delete=models.CASCADE)
    published_date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="upload_file/")
    content=models.TextField()
    def __str__(self):
        return str(self.title+"  "+str(self.published_date))
    #def get_absolute_url(self): 
      #  return reverse('index')
    
    
