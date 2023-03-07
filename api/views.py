from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SkillSerializer
from .models import Skill

@api_view(['GET'])
def skill_list(request):
    skills = Skill.objects.all()
    serializer = SkillSerializer(skills, many=True)
    return Response(serializer.data)
