from django.contrib import admin

from .models import (
    Skill,
    Project,
    AboutMe,
    NewsletterSubscriber
)


admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(AboutMe)
admin.site.register(NewsletterSubscriber)