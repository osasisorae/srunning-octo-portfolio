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
    
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    interests = models.TextField()
    personality_traits = models.TextField()
    education = models.CharField(max_length=100)
    achievements = models.TextField()
    personal_statement = models.TextField()
    
    def __str__(self):
        return self.name
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email