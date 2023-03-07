from django.test import TestCase
from ..models import Skill
from rest_framework.test import APIRequestFactory
from ..views import skill_list
from ..serializers import SkillSerializer
from django.urls import reverse, resolve


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

    def test_skill_list_view(self):
        request = self.factory.get('/api/skills/')
        response = skill_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.skill.name)

class SkillSerializerTestCase(TestCase):

    def setUp(self):
        self.skill_data = {
            'name': 'Python',
            'description': 'A high-level programming language.'
        }
        self.skill = Skill.objects.create(**self.skill_data)
        self.serializer = SkillSerializer(instance=self.skill)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'name', 'description']))

    def test_serializer_data_matches_instance_data(self):
        data = self.serializer.data
        for key, value in self.skill_data.items():
            self.assertEqual(data[key], value)

class SkillURLsTestCase(TestCase):

    def test_skill_list_url_resolves_to_skill_list_view(self):
        url = reverse('skill-list')
        resolver_match = resolve(url)
        self.assertEqual(resolver_match.func, skill_list)
