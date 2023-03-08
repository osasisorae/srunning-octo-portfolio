from django.test import TestCase
from ..models import Skill
from rest_framework.test import APIRequestFactory
from ..views import SkillList
from ..serializers import SkillSerializer
from django.urls import reverse, resolve
from rest_framework import status



class SkillModelTestCase(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name='Python',
            description='A programming language'
        )

    def test_skill_creation(self):
        self.assertTrue(isinstance(self.skill, Skill))
        self.assertEqual(self.skill.__str__(), self.skill.name)

class SkillViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.skill = Skill.objects.create(
            name='Python',
            description='A programming language'
        )

    # def test_skill_list_view(self):
    #     url = reverse('skill-list')
    #     response = self.client.get(url, format='json')
    #     skills = Skill.objects.all()
    #     serializer = SkillSerializer(skills, many=True)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, serializer.data)

class SkillSerializerTestCase(TestCase):

    def setUp(self):
        self.skill_data = {
            'name': 'Python',
            'description': 'A high-level programming language.'
        }
        self.skill = Skill.objects.create(**self.skill_data)
        
    def test_serializer_fields(self):
        fields = ['id', 'name', 'description']
        serializer = SkillSerializer()
        self.assertEqual(list(dict(serializer.fields).keys()), fields)


class SkillURLsTestCase(TestCase):

    def test_skill_list_url_resolves_to_skill_list_view(self):
        url = reverse('skill-list')
        self.assertEqual(resolve(url).func.view_class, SkillList)
