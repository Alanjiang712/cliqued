from django.db import models
import uuid
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class CustomUser(AbstractUser):
    # 用户头像
    useravatar = models.ImageField(upload_to='useravatars/', null=True, blank=True)
    
    # UID UUIDField
    # uid = models.UUIDField(default=uuid.uuid4, unique=True)

    # 个人信息
    age = models.PositiveIntegerField(null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    school = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')), null=True, blank=True)
    
    # 姓名
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=30, blank=True)

class UserPreferences(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    #暂时留空

class ContactUs(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    send_time = models.DateTimeField()
    text_input = models.TextField()