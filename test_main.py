import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def course_manager():
    return MagicMock()

@pytest.fixture
def user_manager():
    return MagicMock()

def test_welcome(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.strip('"') == "Mini Canvas"

def test_create_a_course(client, user_manager, course_manager):
    user_manager.create_a_user = MagicMock(return_value=None)
    response = client.post("/courses/CS101", json={"semester": "Fall 2024", "teacher_id_list": [1, 2]})
    assert response.status_code == 200
    assert response.json()

def test_import_students(client, course_manager):
    course_manager.create_a_course = MagicMock(return_value=None)
    response = client.put("/courses/1/students", json={"student_id_list": [3, 4]})
    assert response.status_code == 200 
    assert response.json()

def test_course_not_found(client, course_manager):
    course_manager.find_a_course = MagicMock(return_value=None)
    response = client.put("/courses/2/students", json={"student_id_list": [3, 4]})
    assert response.status_code == 404
    assert response.json() == {"detail": "Course 2 not found"}

