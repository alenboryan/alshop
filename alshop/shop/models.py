from django.db import models
from datetime import timezone
import datetime
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=150, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
CATEGORIES = [
    ('TShirts', 'T-Shirts'),
    ('Shirts', 'Shirts'),
    ('Sweaters', 'Sweaters'),
    ('Jeans', 'Jeans'),
    ('Jackets', 'Jackets'),
    ('Shoes', 'Shoes'),
]
    
class ForMan(models.Model):
    photo =  models.ImageField(upload_to='images/', blank=True)
    price = models.PositiveIntegerField(blank=False)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    title = models.CharField(max_length=128, default="Untitled")
   
    
class ForWoman(models.Model):
    photo =  models.ImageField(upload_to='images/', blank=True)
    price = models.PositiveIntegerField(blank=False)
    category = models.CharField(max_length=30, choices=CATEGORIES)
    title = models.CharField(max_length=128, default="Untitled")