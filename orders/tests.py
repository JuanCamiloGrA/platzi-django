from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order


class OrderDetailViewTests(TestCase):
    """
    Tests for the OrderDetailView.
    """

    def setUp(self):
        """
        Set up the test environment.
        Create users and an order.
        """
        # Create a user and another user
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.other_user = User.objects.create_user(
            username="otheruser", password="12345"
        )

        # Create an order for the first user
        self.order = Order.objects.create(user=self.user, is_active=True)

        # Set the URL for the view
        self.url = reverse("my_order")

    def test_login_required(self):
        """
        Test that the view requires login.
        """
        # Attempt to access the view without logging in
        response = self.client.get(self.url)

        # Check that the response is not 200 OK
        self.assertNotEqual(response.status_code, 200)

        # Check that the response redirects to the login page
        self.assertRedirects(response, f"/accounts/login/?next={self.url}")

    def test_correct_order_for_logged_in_user(self):
        """
        Test that the view returns the correct order for the logged-in user.
        """
        # Log in as the first user
        self.client.login(username="testuser", password="12345")

        # Access the view
        response = self.client.get(self.url)

        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check that the correct order is returned
        self.assertEqual(response.context["order"], self.order)
