import os
from typing import List

class Config:
    CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", default="path_to_your_csv_file.csv")
    
    # Add the valid categories and test types for your application.
    VALID_SUBJECTS: List[str] = ["BDD", "Systèmes distribués","Docker","Classification","Data Science","Machine Learning","Automation","Streaming de données"]
    VALID_USE_CASES: List[str] = ["Test de positionnement","Test de validation","Total Bootcamp"]
    
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "4dm1N"

    AUTHORIZED_USERS = {
        "alice": "wonderland",
        "bob": "builder",
        "clementine": "mandarine"
    }

# Create an instance of Config class so that we can import it and use in other modules
config = Config()
