import csv
import random
from typing import List, Dict, Any
from config import config

def read_data_from_csv() -> List[Dict[str, Any]]:
    with open(config.CSV_FILE_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def write_data_to_csv(row: Dict[str, Any]):
    with open(config.CSV_FILE_PATH, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=row.keys())
        writer.writerow(row)

def get_random_questions(subjects: List[str], use: str, number: int) -> List[Dict[str, Any]]:
    data = read_data_from_csv()
    filtered_data = [row for row in data if row['subject'] in subjects and row['use'] == use]
    if len(filtered_data) < number:
        raise Exception("Not enough questions available for the requested type and subjects")
    return random.sample(filtered_data, number)
