from django.urls import path
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import RegisterView, LogoutView

from .views import (
    SkillList,
    ProjectList,
    ProjectDetail,
    AboutMeListAPIView,
    NewsletterSubscriberView
)

urlpatterns = [
    # auth
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    
    
    # models
    path('skills/', SkillList.as_view(), name='skill-list'),
    path('projects/', ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),
    path('about-me/', AboutMeListAPIView.as_view(), name='about-list'),
    path('subscribe-newsletter/', NewsletterSubscriberView.as_view(), name='newsletter-subscriber',)
]
