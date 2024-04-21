from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course_success():
    response = client.post("/courses/COSC101", json={"semester": "Spring", "teacher_id_list": [1]})
    assert response.status_code == 200
    assert "course_id" in response.json()

def test_create_course_invalid_teacher():
    response = client.post("/courses/COSC101", json={"semester": "Spring", "teacher_id_list": [100]})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid teacher IDs provided"

def test_import_students_success():
    response = client.put("/courses/1/students", json={"student_id_list": [2, 3]})
    assert response.status_code == 200
    assert response.json() == {"message": "Students imported successfully"}

def test_import_students_invalid_course():
    response = client.put("/courses/100/students", json={"student_id_list": [2, 3]})
    assert response.status_code == 404
    assert response.json()["detail"] == "Course not found"

def test_import_students_invalid_students():
    response = client.put("/courses/1/students", json={"student_id_list": [100, 101]})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid student IDs provided"
