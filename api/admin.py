from django.contrib import admin

from .models import (
    Skill,
    Project,
)


admin.site.register(Skill)
admin.site.register(Project)