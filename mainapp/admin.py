from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Habit, HabitTracking, Match

# Register User
admin.site.register(CustomUser, UserAdmin)

# 注册 Habit 模型
admin.site.register(Habit)

# 注册 HabitTracking 模型
admin.site.register(HabitTracking)

# 注册 Match 模型
admin.site.register(Match)