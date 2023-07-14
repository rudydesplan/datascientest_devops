import coverage
import logging
from fastapi.testclient import TestClient
from main import app

# Configure logging
logging.basicConfig(level=logging.INFO)

client = TestClient(app)


# Test for health check endpoint

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "API is healthy"}
    if response.status_code == 200:
        logging.info("test_health_check PASSED")
    else:
        logging.error("test_health_check FAILED")

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
    if response.status_code == 200:
        logging.info("test_get_questions_unauthorized PASSED")
    else:
        logging.error("test_get_questions_unauthorized FAILED")

def test_get_questions_wrong_credentials():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=5",
        auth=("wrong_user", "wrong_password")
    )
    assert response.status_code == 401

# Test for valid parameters 

def test_get_questions_zero():
    try:
        response = client.get(
            "/questions?subject=BDD&use=Test de positionnement&number=0",
            auth=("alice", "wonderland")
        )
        assert False, "Expected ValueError to be raised"
    except ValueError as error:
        assert str(error) == "Number of questions should be a positive integer."

# Test for invalid parameters 

def test_get_questions_negative_number():
    try:
        response = client.get(
            "/questions?subject=BDD&use=Test de positionnement&number=-5",
            auth=("alice", "wonderland")
        )
        assert False, "Expected ValueError to be raised"
    except ValueError as error:
        assert str(error) == "Number of questions should be a positive integer."


# Test for getting random questions with valid subject and test type

def test_get_questions_valid():
    response = client.get(
        "/questions?subject=BDD&use=Test de positionnement&number=5",
        auth=("alice", "wonderland")
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 5
    
    if response.status_code == 200:
        logging.info("test_get_questions_valid PASSED")
    else:
        logging.error("test_get_questions_valid FAILED")

# Test for getting random questions with invalid subject or test type

def test_get_questions_invalid_subject():
    try:
        response = client.get(
            "/questions?subject=Invalid&use=Test de positionnement&number=5",
            auth=("alice", "wonderland")
        )
        assert False, "Expected ValueError to be raised"
    except ValueError as error:
        assert str(error) == "Invalid subject: Invalid"

def test_get_questions_invalid_use_case():
    try:
        response = client.get(
            "/questions?subject=BDD&use=Invalid&number=5",
            auth=("alice", "wonderland")
        )
        assert False, "Expected ValueError to be raised"
    except ValueError as error:
        assert str(error) == "Invalid use case: Invalid"

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
    
    if response.status_code == 200:
        logging.info("test_get_questions_valid PASSED")
    else:
        logging.error("test_get_questions_valid FAILED")

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
    assert response.status_code == 200
    assert response.json() == {"message": "Question added successfully"}
    
    if response.status_code == 200:
        logging.info("test_create_question_empty_strings PASSED")
    else:
        logging.error("test_create_question_empty_strings FAILED")
        
    
if __name__ == "__main__":
    # Enable logging for the test execution
    logging.getLogger().setLevel(logging.INFO)
    logging.info("Starting test execution...")
    
    # Start coverage before your tests
    cov = coverage.Coverage()
    cov.start()
    
    logging.info("Running test_health_check")
    test_health_check()
    
    logging.info("Running test_get_questions_unauthorized")
    test_get_questions_unauthorized()
    
    logging.info("Running test_get_questions_authorized")
    test_get_questions_authorized()
    
    logging.info("Running test_get_questions_wrong_credentials")
    test_get_questions_wrong_credentials()
    
    logging.info("Running test_get_questions_zero")
    test_get_questions_zero()
    
    logging.info("Running test_get_questions_negative_number")
    test_get_questions_negative_number()
    
    logging.info("Running test_get_questions_valid")
    test_get_questions_valid()
    
    logging.info("Running test_get_questions_invalid_subject")
    test_get_questions_invalid_subject()
    
    logging.info("Running test_get_questions_invalid_use_case")
    test_get_questions_invalid_use_case()
    
    logging.info("Running test_create_question_unauthorized")
    test_create_question_unauthorized()
    
    logging.info("Running test_create_question_authorized")
    test_create_question_authorized()
    
    logging.info("Running test_create_question_missing_parameters")
    test_create_question_missing_parameters()
    
    logging.info("Running test_create_question_empty_strings")
    test_create_question_empty_strings()
    
    logging.info("Test execution completed.")
    
    # At the end of your tests, stop and save coverage data
    cov.stop()
    cov.save()

    # Generate the coverage report
    cov.report()
