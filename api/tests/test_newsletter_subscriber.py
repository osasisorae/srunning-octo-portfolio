from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import NewsletterSubscriber

class NewsletterSubscriberViewTest(APITestCase):
    def test_create_newsletter_subscriber(self):
        url = reverse('newsletter-subscriber')
        data = {'email': 'test@example.com'}

        # Ensure that a POST request with valid data creates a new subscriber
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NewsletterSubscriber.objects.count(), 1)
        self.assertEqual(NewsletterSubscriber.objects.get().email, 'test@example.com')

        # Ensure that a POST request with an email that already exists returns an error
        response = self.client.post(url, data)
        # print('Response Status: {}'.format(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], "newsletter subscriber with this email already exists.")
