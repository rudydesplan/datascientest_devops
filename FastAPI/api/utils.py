from typing import List
from config import config

def validate_subjects(subjects: List[str]):
    for subject in subjects:
        if subject not in config.VALID_SUBJECTS:
            raise ValueError(f"Invalid subject: {subject}")

def validate_use_case(use_case: str):
    if use_case not in config.VALID_USE_CASES:
        raise ValueError(f"Invalid use case: {use_case}")

def validate_number_of_questions(number: int):
    if number <= 0:
        raise ValueError("Number of questions should be a positive integer.")
