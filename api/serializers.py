from rest_framework import serializers
from mainapp.models import CustomUser, Habit, HabitTracking, Match

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'useravatar']

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

class HabitTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitTracking
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'
