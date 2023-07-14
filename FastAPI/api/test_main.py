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
    response = client.get("/questions?subject=BDD&use=Test de positionnement&number=5")
    assert response.status_code == 401

def test_get_questions_authorized():
    response = client.get(
        "/questions",
        params={
            "subject": "Classification",
            "use": "Test de validation",
            "number": 5,
        },
        headers={"Authorization": "Basic YWxpY2U6d29uZGVybGFuZA=="}
    )
    assert response.status_code == 200

def test_get_questions_wrong_credentials():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=5",
        auth=("wrong_user", "wrong_password")
    )
    assert response.status_code == 401

# Test for valid parameters 

def test_get_questions_zero():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=0",
        auth=("alice", "wonderland")
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == []

# Test for invalid parameters 

def test_get_questions_negative_number():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=-5",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 400

# Test for getting random questions with valid subject and test type

def test_get_questions_valid():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=5",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 5

# Test for getting random questions with invalid subject or test type

def test_get_questions_invalid_subject():
    response = client.get(
        "/questions?subject=Invalid&use=Test de positionnement&number=5",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 400

def test_get_questions_invalid_use_case():
    response = client.get(
        "/questions?subject=BDD&use=Invalid&number=5",
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
            "correct": "A",
            "use": "Test de positionnement",
            "responseA": "Response A",
            "responseB": "Response B",
            "responseC": "Response C",
            "responseD": "Response D",
            "remark": ""
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
            "correct": "A",
            "use": "Test de positionnement",
            "responseA": "Response A",
            "responseB": "Response B",
            "responseC": "Response C",
            "responseD": "Response D",
            "remark": ""
        },
        auth=("admin", "4dm1N")
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Question added successfully"}

def test_create_question_missing_parameters():
    response = client.post(
        "/admin",
        json={
            "question": "Test question",
            "correct": "A",
            "use": "Test de positionnement",
            "responseA": "Response A",
            "responseB": "Response B",
            "responseC": "Response C",
            "responseD": "Response D",
            "remark": ""
        },
        auth=("admin", "4dm1N")
    )
    assert response.status_code == 422

def test_create_question_empty_strings():
    response = client.post(
        "/admin",
        json={
            "question": "",
            "subject": "",
            "correct": "",
            "use": "",
            "responseA": "",
            "responseB": "",
            "responseC": "",
            "responseD": "",
            "remark": ""
        },
        auth=("admin", "4dm1N")
    )
    assert response.status_code == 422
