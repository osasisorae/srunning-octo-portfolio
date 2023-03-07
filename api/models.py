from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # add any other relevant fields here

    def __str__(self):
        return self.name