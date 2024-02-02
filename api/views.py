from rest_framework import viewsets
from mainapp.models import CustomUser, Habit, HabitTracking, Match
from .serializers import CustomUserSerializer, HabitSerializer, HabitTrackingSerializer, MatchSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

class HabitTrackingViewSet(viewsets.ModelViewSet):
    queryset = HabitTracking.objects.all()
    serializer_class = HabitTrackingSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
