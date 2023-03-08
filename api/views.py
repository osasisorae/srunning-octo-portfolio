from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SkillSerializer
from .models import Skill

from rest_framework import generics
from .models import Project
from .serializers import ProjectSerializer


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = ProjectSerializer


class ProjectList(generics.ListAPIView):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
