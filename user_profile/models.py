from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class CustomUser(AbstractBaseUser):
    '''
    Custom user class.
    '''
    username = models.CharField('username', max_length=10,unique=True, db_index= True)
    email = models.EmailField('email_address', unique = True)
    joined_on = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    is_admin =  models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username