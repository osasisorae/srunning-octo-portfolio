from django.urls import path
from .views import skill_list

urlpatterns = [
    path('skills/', skill_list, name='skill-list'),
]
