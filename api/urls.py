from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'habits', views.HabitViewSet)
router.register(r'habittrackings', views.HabitTrackingViewSet)
router.register(r'matches', views.MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
