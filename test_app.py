import pytest
from app import add, app

def test_add_success():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_app_index():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
