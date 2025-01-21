# LinkedIn Company Parser API

This project is a FastAPI-based web application that parses company data from LinkedIn and stores it in a MongoDB database.

## Project Structure

```
_httpreq/
.gitignore
app/
    __pycache__/
    database.py
    main.py
    models.py
    parsers.py
    routes.py
README.md
```

## Files

- `app/main.py`: The main entry point of the FastAPI application.
- `app/routes.py`: Defines the API routes for parsing company data and retrieving stored company data.
- `app/parsers.py`: Contains the logic for parsing company data from LinkedIn using Playwright.
- `app/models.py`: Defines the Pydantic models for the company and employee data.
- `app/database.py`: Contains the functions for interacting with the MongoDB database.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install fastapi uvicorn pymongo playwright
    ```

4. Install the necessary browser binaries for Playwright:
    ```sh
    playwright install
    ```

5. Start the MongoDB server:
    ```sh
    mongod --dbpath <path-to-your-db-directory>
    ```

## Running the Application

1. Start the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to see the welcome message.

## API Endpoints

- `GET /`: Returns a welcome message.
- `POST /parse`: Parses company data from the provided LinkedIn URL and stores it in the database.
- `GET /company/{company_name}`: Retrieves the stored company data by company name.

## Example Usage

1. Parse company data:
    ```sh
    curl -X POST "http://127.0.0.1:8000/parse" -H "Content-Type: application/json" -d '{"company_url": "https://www.linkedin.com/company/example"}'
    ```

2. Get company data:
    ```sh
    curl -X GET "http://127.0.0.1:8000/company/example"
    ```

## License

This project is licensed under the MIT License.