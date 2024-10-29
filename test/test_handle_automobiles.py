import json
from app import app  # Replace 'your_flask_app' with the actual name of your app file

class TestAutomobileAPI:
    @classmethod
    def setup_class(cls):
        cls.client = app.test_client()

    def test_get_all_automobiles(self):
        response = self.client.get('/automobiles')
        assert response.status_code == 200

    def test_add_automobile(self):
        response = self.client.post('/automobiles', json={"make": "Ford", "model": "Fusion", "year": 2021})
        assert response.status_code == 201

    def test_update_automobile(self):
        response = self.client.put('/automobiles/1', json={"model": "Camry"})
        assert response.status_code == 200

    def test_delete_automobile(self):
        response = self.client.delete('/automobiles/1')
        assert response.status_code == 200


