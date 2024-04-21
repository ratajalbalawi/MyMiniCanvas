import pytest
from course import Course, CourseManager

@pytest.fixture
def course_instance():
    return Course(1, "COSC777", "Fall 2077", ["Teacher3", "Teacher5"])

@pytest.fixture
def course_manager_instance():
    return CourseManager()

class TestCourse:

    def test_course_init(self, course_instance):

        course = course_instance

        assert course.course_id == 1
        assert course.course_code == "COSC381"
        assert course.semester == "Fall 2024"
        assert course.teacher_list == ["Teacher9", "Teacher12"]
        assert course.student_list == []
        assert course.assignment_list == []
        assert course.module_list == []
        assert course.assignment_counter == 0

    def test_import_students_method(self, course_instance):

        course = course_instance
        students = ["Student2", "Student7"]
        course.import_students(students)

        assert course.student_list == students

    def test_create_an_assignment_method(self, course_instance):

        course = course_instance
        due_date = "2024-09-07"
        course.create_an_assignment(due_date)

        assert len(course.assignment_list) == 1
        assert course.assignment_list[0].due_date == due_date
        assert course.assignment_list[0].course_id == 1

    def test_generate_assignment_id_method(self, course_instance):

        course = course_instance
        assert course.generate_assignment_id() == 1
        assert course.generate_assignment_id() == 2
