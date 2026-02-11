from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    photo = models.ImageField(upload_to='users/')
    phone_number = models.CharField(max_length=15, default='+996')
    
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=100, choices=GENDER, default='MALE')
    city = models.CharField(max_length=100, default='Бишкек')
    resume = models.CharField(max_length=100, default='Меня зовут ...')
    
    KNOWLEDGE_5 = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    knowledge_5 = models.CharField(max_length=100, choices=KNOWLEDGE_5, default='1')
    passport = models.CharField(max_length=25, default='1234567')

    def __str__(self):
        return self.username