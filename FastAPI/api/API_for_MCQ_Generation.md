# Architecture

Since we're dealing with a CSV file as the database, a serverless, microservices architecture would be beneficial but for this exercie that is not the case .

## Database

The current database is a CSV file, but it could be a good idea to move this data into a SQL or NoSQL database to improve data handling and management.

PostgreSQL or MongoDB could be good options.

## API

We'll use FastAPI to create the API.

FastAPI provides automatic interactive API documentation (with Swagger UI and ReDoc).

It also comes with OAuth2 password flow built-in, which can be used for Basic Authentication.

## Data Processing

The data is stored in a CSV file. Python has a built-in CSV module that we can use for reading data from and writing data to CSV files.

For reading data, we will use csv.DictReader which allows us to access rows as Python dictionaries.

When writing data, we will use csv.DictWriter for convenience.

If the dataset was large and/or we would need to perform complex operations on your data (like grouping, aggregation, merging etc.), pandas would be the better option.

## Authentication

FastAPI provides several tools out of the box for implementing security and authentication in our API.

For implementing Basic Authentication, we will use HTTPBasic scheme from FastAPI's fastapi.security module.

We will keep a dictionary for storing username and password pairs.

## Fetching Questions

We will use Python's built-in random module to pick a specified number of random questions from the CSV file based on the test type (use) and categories (subject).

We'll implement this in a utility function.

## Admin Operations

The API will have a special endpoint for admin operations.
Only the admin user can use this endpoint to add new questions to the CSV file.

## Documentation

FastAPI automatically generates an interactive API documentation when you run the application.

We will make sure all the endpoints are well-documented by adding docstrings and annotations

## Error Handling

FastAPI provides automatic request validation and error handling.

We just need to define the expected request bodies and parameters using Python type hints and FastAPI will take care of the rest.

## Testing

FastAPI also provides built-in support for test client based on requests.

We can write test cases using this test client and run them to make sure our API is working as expected.

## Required Libraries

We'll specify these in a `requirements.txt` file

# Application Structure

`main.py`: This is the entry point for the application. It will initialize the FastAPI application and include the routers from other modules.

`auth.py`: This module will contain the logic for basic authentication, such as verifying the username and password from the Authorization header.

`admin.py`: This module will provide the admin endpoints, specifically the endpoint for creating a new question.

`database.py`: This module will handle all the operations related to the database (CSV file in this case), such as reading data from the CSV file, writing new data to the CSV file, and selecting random questions.

`questions.py`: This module will contain the logic for question-related operations, such as fetching questions based on the selected test type and categories.

`models.py`: This module will define Pydantic models which will be used for request and response handling. Pydantic is a data validation library provided by FastAPI that will handle request validation for us.

`config.py`: This module will contain all the configuration variables for the application, such as the location of the CSV file, the valid test types and categories, and the admin password.

`utils.py`: This module will contain utility functions that are used throughout the application. One such function could be for selecting a specified number of random questions.

`requirements.txt`

# Development process

config.py: Set up our configuration variables first. This can include the location of your CSV file, the valid test types and categories, and the admin password.

models.py: Define our Pydantic models next. These models will be used for request and response handling in your other modules.

database.py: Set up the functionality for reading and writing from your CSV file. This module is the cornerstone of your data handling, and many of your other modules will rely on it.

auth.py: Set up our basic authentication logic. This will be important to have in place when you start setting up endpoints in your other modules.

utils.py: Write utility functions for operations like fetching random questions. Many of our endpoints may need to use these functions, so it's good to have them in place early.

questions.py and admin.py: Write the logic for the question-related operations and the admin operations. These are the main features of the application and will rely on all of the previous modules we have written.

main.py: Once all our other modules are in place, we can write the main.py file. This file will bring everything together and serve as the entry point for your application.

requirements.txt: This can be created at any time during the project, but you should certainly have it in place before anyone else tries to run your application. It should list all of the Python libraries that your application depends on.
