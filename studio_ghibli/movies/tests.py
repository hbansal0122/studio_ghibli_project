import json
from django.test import TestCase, Client
from unittest.mock import Mock, patch
from .api_data.api import get_films, get_people
from .api_data.get_movie_data import get_movie_data
from .test_data import stub_films, stub_poeple


class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code
        
class ViewTests(TestCase):
    """ Test the functionality on unit level basis"""
    def test_error_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page(self):
        response = self.client.get('/movies/')        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Movies and their Cast", html=True)

    def test_ghibli_films_response(self):
        self.assertEqual(get_films().status_code, 200)

    def test_ghibli_people_response(self):
        self.assertEqual(get_people().status_code, 200)

    def test_complete_custom_response(self):
        response = get_movie_data(MockResponse(json.dumps(stub_films), 200), 
        MockResponse(json.dumps(stub_poeple), 200))
        self.assertEqual(response["is_success"], True)
        self.assertEqual(len(response["movies"]), 2)
        self.assertEqual(len(response["movies"][0]["people"]), 3)
        self.assertEqual(len(response["movies"][1]["people"]), 2)
    
    def test_complete_custom_status_404(self):
        response = get_movie_data(MockResponse(json.dumps({}), 404), MockResponse(json.dumps({}), 200))
        self.assertEqual(response["is_success"], False)
        self.assertEqual(len(response["movies"]), 0)

    def test_complete_custom_empty_response(self):
        response = get_movie_data(MockResponse(json.dumps({}), 200), MockResponse(json.dumps({}), 200))
        self.assertEqual(response["is_success"], False)
        self.assertEqual(len(response["movies"]), 0)