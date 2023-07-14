import csv
import random
from typing import List, Dict, Any
from config import config
from fastapi import HTTPException

def read_data_from_csv() -> List[Dict[str, Any]]:
    try:
        with open(config.CSV_FILE_PATH, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return list(reader)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="CSV file not found")
    except csv.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while reading the CSV file: {str(e)}")

def write_data_to_csv(row: Dict[str, Any]):
    try:
        with open(config.CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=row.keys())
            writer.writerow(row)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="CSV file not found")
    except csv.Error as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while writing to the CSV file: {str(e)}")

def get_random_questions(subjects: List[str], use: str, number: int) -> List[Dict[str, Any]]:
    try:
        data = read_data_from_csv()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    filtered_data = [row for row in data if row['subject'] in subjects and row['use'] == use]
    if len(filtered_data) < number:
        raise Exception("Not enough questions available for the requested type and subjects")
    return random.sample(filtered_data, number)
