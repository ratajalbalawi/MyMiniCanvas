import pytest
from assignment import Assignment, Submission

@pytest.fixture
def sample_assignment():
    return Assignment(1, "2024-09-07", "COSC381")

class TestAssignment:

    def test_assignment_init(self, sample_assignment):

        assert sample_assignment.assignment_id == 1
        assert sample_assignment.due_date == "2024-09-07"
        assert sample_assignment.course_id == "COSC381"
        assert sample_assignment.submission_list == []

    def test_submit_method(self, sample_assignment):

        submission = Submission(1, "Content")
        sample_assignment.submit(submission)

        assert len(sample_assignment.submission_list) == 1
        assert sample_assignment.submission_list[0] == submission

class TestSubmission:

    def test_submission_init(self):

        submission = Submission(1, "Content")
        assert submission.student_id == 1
        assert submission.submission == "Content"
        assert submission.grade == -1.0
