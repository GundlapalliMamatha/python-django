from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import response
from rest_framework.status import HTTP_204_NO_CONTENT

from .models import UserProfile
from .serializers import SkillCapitalSerializer
# Create your views here.

class SkillCapitalViewSet(viewsets.ModelViewSet):

    queryset = UserProfile.objects.all()
    serializer_class = SkillCapitalSerializer

    def destroy(self, request, pk=None):
        
        instance = self.get_object()
        instance.delete()

        return response.Response({'messsage':"Record delete successfully"},status=HTTP_204_NO_CONTENT)