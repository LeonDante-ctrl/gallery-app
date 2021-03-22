from django.test import TestCase
from index.models import *
from django.urls import reverse


class TestIndexView(TestCase):

    def setUp(self):
        self.view_name = "welcome"
        self.route = ""
        self.template_name = "index.html"

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(self.route)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse(self.view_name))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse(self.view_name))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, self.template_name)


class TestSearchView(TestCase):
    """
    test if view url exists at desired location
    """

    def setUp(self):
        self.view_name = "search_results"
        self.route = "/search?image=iron"
        self.template_name = "results.html"

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get(self.route)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse(self.view_name))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse(self.view_name))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, self.template_name)
