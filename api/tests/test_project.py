from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Project
from ..serializers import ProjectSerializer
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import ProjectList
from rest_framework.test import APIClient
from django.contrib.auth.models import User


class ProjectModelTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(
                username='testuser1',
                password='agoodtest7576'
            )
        self.test_user.save()
        
        self.project = Project.objects.create(
            user=self.test_user,
            title='Test Project',
            description='This is a test project',
            start_date='2022-01-01',
            end_date='2022-01-31',
            is_ongoing=False
        )
        self.project.save()
        
    def test_project_user(self):
        self.assertEqual(self.project.user.get_username(), 'testuser1')
    
    def test_project_title(self):
        self.assertEqual(self.project.title, 'Test Project')

    def test_project_description(self):
        self.assertEqual(self.project.description, 'This is a test project')

    def test_project_start_date(self):
        self.assertEqual(str(self.project.start_date), '2022-01-01')

    def test_project_end_date(self):
        self.assertEqual(str(self.project.end_date), '2022-01-31')

    def test_project_is_ongoing(self):
        self.assertFalse(self.project.is_ongoing)
        
    def test_get_project_list(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        

class ProjectSerializerTest(APITestCase):
    def test_serializer_fields(self):
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'is_ongoing', 'created_at']
        serializer = ProjectSerializer()
        self.assertEqual(list(dict(serializer.fields).keys()), fields)


class TestProjectUrl(TestCase):
    def test_project_list_url_resolves(self):
        url = reverse('project-list')
        self.assertEqual(resolve(url).func.view_class, ProjectList)
        
class ProjectDetailTest(TestCase):
    def setUp(self):
        
        self.test_user = User.objects.create_user(
                username='testuser1',
                password='agoodtest7576'
            )
        self.test_user.save()
        
        self.project1 = Project.objects.create(
            user=self.test_user,
            title='Test Project',
            description='This is a test project',
            start_date='2022-01-01',
            end_date='2022-01-31',
            is_ongoing=False
        )
        self.project1.save()
        
        self.project2 = Project.objects.create(
            user=self.test_user,
            title='Test Project 2',
            description='This is a test project Two',
            start_date='2022-01-01',
            end_date='2022-01-31',
            is_ongoing=False
        )
        self.project2.save()
        
        self.client = APIClient()

    def test_get_project_detail(self):
        url = reverse('project-detail', kwargs={'pk': self.project1.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProjectSerializer(self.project1).data)

    def test_get_invalid_project_detail(self):
        url = reverse('project-detail', kwargs={'pk': 100})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

