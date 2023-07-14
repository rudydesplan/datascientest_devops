from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test for health check endpoint

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is healthy"}

# Test for basic authentication

def test_get_questions_unauthorized():
    response = client.get("/questions?subjects=BDD&use=Test de positionnement&number=10")
    assert response.status_code == 401

def test_get_questions_authorized():
    response = client.get(
        "/questions?subjects=BDD&use=Test de positionnement&number=10",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 200

# Test for getting random questions with valid subjects and test type

def test_get_questions_valid():
    response = client.get(
        "/questions?subjects=BDD&use=Test de positionnement&number=10",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 10

# Test for getting random questions with invalid subjects or test type

def test_get_questions_invalid_subjects():
    response = client.get(
        "/questions?subjects=Invalid&use=Test de positionnement&number=10",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 400

def test_get_questions_invalid_use_case():
    response = client.get(
        "/questions?subjects=BDD&use=Invalid&number=10",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 400

# Test for admin operations (creating a new question)

def test_create_question_unauthorized():
    response = client.post(
        "/admin",
        json={
            "question": "Test question",
            "subject": "BDD",
            "correct": ["A"],
            "use": "Test de positionnement",
            "answerA": "Answer A",
            "answerB": "Answer B",
            "answerC": "Answer C",
            "answerD": "Answer D"
        },
        auth=("alice", "wonderland")
    )
    assert response.status_code == 403

def test_create_question_authorized():
    response = client.post(
        "/admin",
        json={
            "question": "Test question",
            "subject": "BDD",
            "correct": ["A"],
            "use": "Test de positionnement",
            "answerA": "Answer A",
            "answerB": "Answer B",
            "answerC": "Answer C",
            "answerD": "Answer D"
        },
        auth=("admin", "4dm1N")
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Question added successfully"}
