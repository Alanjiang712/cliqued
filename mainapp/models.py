from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    # 用户头像
    useravatar = models.ImageField(upload_to='useravatars/', null=True, blank=True)
    
    # UID UUIDField
    # uid = models.UUIDField(default=uuid.uuid4, unique=True)

class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    habit_title = models.CharField(max_length=255)
    habit_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    reminder_enabled = models.BooleanField(default=False)
    reminder_time = models.TimeField(null=True, blank=True)

    progress_count = models.IntegerField(default=0)

    def __str__(self):
        return self.habit_title

