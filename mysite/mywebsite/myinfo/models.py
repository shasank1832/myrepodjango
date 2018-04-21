from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    Email =models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    comment_about_me=models.TextField()
    
    def __str__(self):
        return self.name
