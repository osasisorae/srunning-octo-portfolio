from rest_framework.response import Response
from .serializers import (
    SkillSerializer,
    ProjectSerializer,
    AboutMeSerializer,
    NewsletterSubscriberSerializer
)
from .models import (
    Skill,
    Project,
    AboutMe,
    NewsletterSubscriber
)
from rest_framework import (
    generics,
    status,
)


class SkillList(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectList(generics.ListAPIView):
    
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class AboutMeListAPIView(generics.ListAPIView):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer



class NewsletterSubscriberView(generics.CreateAPIView):
    serializer_class = NewsletterSubscriberSerializer
    queryset = NewsletterSubscriber.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the email is already subscribed
        email = serializer.validated_data['email']
        if NewsletterSubscriber.objects.filter(email=email).exists():
            return Response({'email': ['This email address is already subscribed.']}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)