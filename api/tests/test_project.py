from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Project
from ..serializers import ProjectSerializer
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import ProjectList

class ProjectModelTest(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='This is a test project',
            start_date='2022-01-01',
            end_date='2022-01-31',
            is_ongoing=False
        )

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

class ProjectSerializerTest(APITestCase):
    def test_serializer_fields(self):
        fields = ['id', 'title', 'description', 'start_date', 'end_date', 'is_ongoing', 'created_at']
        serializer = ProjectSerializer()
        self.assertEqual(list(dict(serializer.fields).keys()), fields)

class ProjectViewTest(APITestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title='Test Project',
            description='This is a test project',
            start_date='2022-01-01',
            end_date='2022-01-31',
            is_ongoing=False
        )

    def test_get_project_list(self):
        url = reverse('project-list')
        response = self.client.get(url, format='json')
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
class TestProjectUrl(TestCase):
    def test_project_list_url_resolves(self):
        url = reverse('project-list')
        self.assertEqual(resolve(url).func.view_class, ProjectList)