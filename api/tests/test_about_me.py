from django.test import TestCase
from ..models import AboutMe
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..serializers import AboutMeSerializer


class AboutMeModelTestCase(TestCase):
    
    def setUp(self):
        self.aboutme = AboutMe.objects.create(
            name='John Doe',
            age=25,
            location='New York',
            occupation='Software Engineer',
            interests='Programming, reading, hiking',
            personality_traits='Creative, curious, determined',
            education='Bachelor of Science in Computer Science',
            achievements='Won the Hackathon 2021, Developed an app that got 100k+ downloads',
            personal_statement='I believe in the power of technology to improve people\'s lives.'
        )
    
    def test_aboutme_fields(self):
        self.assertEqual(self.aboutme.name, 'John Doe')
        self.assertEqual(self.aboutme.age, 25)
        self.assertEqual(self.aboutme.location, 'New York')
        self.assertEqual(self.aboutme.occupation, 'Software Engineer')
        self.assertEqual(self.aboutme.interests, 'Programming, reading, hiking')
        self.assertEqual(self.aboutme.personality_traits, 'Creative, curious, determined')
        self.assertEqual(self.aboutme.education, 'Bachelor of Science in Computer Science')
        self.assertEqual(self.aboutme.achievements, 'Won the Hackathon 2021, Developed an app that got 100k+ downloads')
        self.assertEqual(self.aboutme.personal_statement, 'I believe in the power of technology to improve people\'s lives.')
    
    def test_aboutme_str(self):
        self.assertEqual(str(self.aboutme), 'John Doe')


class AboutMeTestCase(TestCase):
    def setUp(self):
        self.aboutme = AboutMe.objects.create(
            name='John Doe',
            age=25,
            location='New York',
            occupation='Software Engineer',
            interests='Programming, Reading, Traveling',
            personality_traits='Ambitious, Analytical, Responsible',
            education='Bachelor of Computer Science',
            achievements='Completed a coding bootcamp, Published a research paper',
            personal_statement='I am passionate about creating useful software that solves real-world problems.'
        )

    def test_aboutme_serializer(self):
        serializer_data = AboutMeSerializer(instance=self.aboutme).data
        expected_data = {
            'id': self.aboutme.id,
            'name': 'John Doe',
            'age': 25,
            'location': 'New York',
            'occupation': 'Software Engineer',
            'interests': 'Programming, Reading, Traveling',
            'personality_traits': 'Ambitious, Analytical, Responsible',
            'education': 'Bachelor of Computer Science',
            'achievements': 'Completed a coding bootcamp, Published a research paper',
            'personal_statement': 'I am passionate about creating useful software that solves real-world problems.'
        }
        self.assertEqual(serializer_data, expected_data)

    def test_aboutme_list_api_view(self):
        client = APIClient()
        url = reverse('about-list')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        expected_data = {
            'id': self.aboutme.id,
            'name': 'John Doe',
            'age': 25,
            'location': 'New York',
            'occupation': 'Software Engineer',
            'interests': 'Programming, Reading, Traveling',
            'personality_traits': 'Ambitious, Analytical, Responsible',
            'education': 'Bachelor of Computer Science',
            'achievements': 'Completed a coding bootcamp, Published a research paper',
            'personal_statement': 'I am passionate about creating useful software that solves real-world problems.'
        }
        self.assertEqual(response.data[0], expected_data)
