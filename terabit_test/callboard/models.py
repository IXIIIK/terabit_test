from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Category(models.Model):
    '''Category model'''
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category


class Advertisment(models.Model):
    '''Advertisment model'''
    STATUS_CHOICED = [
        ('pending', 'Заявок нет'),
        ('accepted', 'Принято'),
        ('rejected', 'Отклонено'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1024)
    image = models.ImageField(upload_to='img/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICED, default='pending')
    created_at = models.DateTimeField(default=datetime.now()) 
    application = models.ManyToManyField(User, related_name='all_applications', blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    

class Requests(models.Model):
    '''Requsts model'''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisment = models.ForeignKey(Advertisment, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Request by {self.user} on {self.advertisment}"


class Comments(models.Model):
    '''Comments model'''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    advertisment_id = models.ForeignKey(Advertisment, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True) 
  
    def __str__(self):  
        return f'Комментарий от {self.user_id.username} на {self.advertisment_id.name}'



    







