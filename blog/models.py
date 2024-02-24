from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


STATUS = (
    (0, 'Draft'),
    (1, 'Publish'),
    (2, 'Delete')
)

class Post(models.Model):
    
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200 , unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField()
    content = models.TextField()
    metadates = models.CharField(max_length=300, default='new post')
    status = models.IntegerField(choices=STATUS, default=0) 



    class Mata:
        ordering = ['-created_on']
        
    
    def __str__(self):
        return self.title
    

