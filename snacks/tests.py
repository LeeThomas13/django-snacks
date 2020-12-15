from django.test import TestCase, Client
import pytest

def test_home_page():
    c = Client()
    response = c.post('')
    assert response == '200'

def test_about_page():
    c = Client()
    response = c.post('/about')
    assert response == '200'

def test_template_home():
    with self.assertTemplateUsed('home.html'):
        render_to_string('home.html')

def test_template_about():
    with self.assertTemplateUsed('about.html'):
        render_to_string('about.html')