from rest_framework.response import Response
from .serializers import (
    SkillSerializer,
    ProjectSerializer,
    AboutMeSerializer
)
from .models import (
    Skill,
    Project,
    AboutMe,
)
from rest_framework import generics


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectList(generics.ListAPIView):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer



