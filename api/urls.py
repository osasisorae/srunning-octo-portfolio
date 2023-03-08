from django.urls import path
from .views import (
    SkillList,
    ProjectList
)

urlpatterns = [
    path('skills/', SkillList.as_view(), name='skill-list'),
    path('projects/', ProjectList.as_view(), name='project-list'),
]
