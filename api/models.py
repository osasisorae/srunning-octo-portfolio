from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # add any other relevant fields here

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_ongoing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return self.title