Navigate to the api folder

# 1 . Install the required libraries:

Run pip install -r requirements.txt to install the necessary libraries specified in the requirements.txt file.

# 2 . Set up the CSV file: 

Make sure you have the CSV file containing the questions and its path is correctly specified in the config.py file (CSV_FILE_PATH variable).
If needed, adjust the path in the config.py file to match the actual location of the CSV file.

# 3 . Run the test : 

Run python test_main.py

# 4. Launch the API:

Run the command uvicorn main:app --reload

The API will start running on http://localhost:8000.

Explore the API documentation: Open a web browser and go to http://localhost:8000/docs.

You will see the automatically generated interactive API documentation (Swagger UI).
