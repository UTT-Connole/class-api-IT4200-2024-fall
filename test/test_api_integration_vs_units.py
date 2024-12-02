import unittest
from flask import json
from app import create_app

class TestNetflixShowsIntegrationVsUnits(unittest.TestCase):
    def setUp(self):
        # Initialize the Flask application
        self.app = create_app()
        self.client = self.app.test_client()

    # Integration Test: Tests the full functionality of the endpoint
    def test_get_random_show_integration(self):
        """
        Integration Test: Ensures the entire endpoint works as expected when no filters are provided.
        """
        response = self.client.get('/netflix-shows')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("netflix_show", data)
        self.assertIn("title", data["netflix_show"])
        self.assertIn("fact", data["netflix_show"])

    def test_get_filtered_show_integration(self):
        """
        Integration Test: Verifies the endpoint with a valid title filter.
        """
        response = self.client.get('/netflix-shows?title=Stranger')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn("netflix_show", data)
        self.assertEqual(data["netflix_show"]["title"], "Stranger Things")

    # Unit Test: Focuses on the filtering logic
    def test_filter_logic_unit(self):
        """
        Unit Test: Directly tests the filtering logic without the full endpoint.
        """
        # Simulate Netflix shows data
        netflix_shows = [
            {"title": "Stranger Things", "fact": "The Demogorgon suit was mostly practical effects."},
            {"title": "The Witcher", "fact": "Henry Cavill performed many of his own stunts."},
        ]
        title_filter = "Witcher"

        # Filtering logic
        filtered_shows = [show for show in netflix_shows if title_filter.lower() in show["title"].lower()]

        self.assertEqual(len(filtered_shows), 1)
        self.assertEqual(filtered_shows[0]["title"], "The Witcher")

    # Unit Test: Simulating a case where no match is found
    def test_filter_logic_no_match_unit(self):
        """
        Unit Test: Ensures filtering logic returns an empty list when no matches are found.
        """
        netflix_shows = [
            {"title": "Stranger Things", "fact": "The Demogorgon suit was mostly practical effects."},
            {"title": "The Witcher", "fact": "Henry Cavill performed many of his own stunts."},
        ]
        title_filter = "NonExistent"

        # Filtering logic
        filtered_shows = [show for show in netflix_shows if title_filter.lower() in show["title"].lower()]

        self.assertEqual(len(filtered_shows), 0)

if __name__ == '__main__':
    unittest.main()
