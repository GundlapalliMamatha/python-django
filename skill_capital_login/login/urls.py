from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillCapitalViewSet

router = DefaultRouter()

router.register(r'login', SkillCapitalViewSet)

urlpatterns = [
    path('', include(router.urls))
]