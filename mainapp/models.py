from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser

class CustomUser(AbstractUser):
    # 用户头像
    useravatar = models.ImageField(
        upload_to='useravatars/', null=True, blank=True)

    # UID UUIDField
    # uid = models.UUIDField(default=uuid.uuid4, unique=True)


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='habits')
    habit_title = models.CharField(max_length=255)
    habit_description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    reminder_enabled = models.BooleanField(default=False)
    reminder_time = models.TimeField(null=True, blank=True)

    progress_count = models.IntegerField(default=0)

    def __str__(self):
        return self.habit_title


class HabitTracking(models.Model):
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)
    date = models.DateField()
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Missed', 'Missed'),
    )
    picture = models.ImageField(
        upload_to='diaryimages/', blank=True, null=True)

    def __str__(self):
        return f"{self.habit.habit_title} on {self.date}"


class Match(models.Model):
    user1 = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_user1')
    user2 = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='matches_user2')
    match_date = models.DateField()
    STATUS_CHOICES = (
        ('Matching', 'Matching'),
        ('Matched', 'Matched'),
        ('Match_off', 'Match_off'),
    )

    def __str__(self):
        return f"Match between {self.user1.username} and {self.user2.username} on {self.match_date}"
