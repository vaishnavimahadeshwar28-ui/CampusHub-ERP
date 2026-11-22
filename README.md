# CampusHub ERP – College Management System

## 1. Project Overview

CampusHub ERP is a College Management System developed using Python, FastAPI and SQLite.

It manages four main modules:
- Student Management
- Faculty Management
- Course Management
- Enrollment Management

The project demonstrates Python programming concepts, database management, REST APIs, asynchronous operations, JSON handling, report generation and unit testing.

## 2. Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- JSON
- Pytest

## 3. Project Setup

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the virtual environment (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

Run the following command:

```bash
python -m app.main
```

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

## 5. Run Unit Tests

```bash
python -m pytest -v
```

## 6. Generate Reports

```bash
python -m app.utils.report_service
```

Generated reports are stored in the `reports` folder.

## 7. Asynchronous Operations

```bash
python -m app.services.async_service
```

This executes asynchronous data retrieval operations for all four modules.

## 8. JSON Import

```bash
python -m app.utils.importer
```

The application supports JSON data import and export for Students, Faculty, Courses and Enrollments.

JSON files are stored in the `data` folder.

## 9. Project Structure

```text
CampusHubERP_Complete/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── data/
├── reports/
├── logs/
├── tests/
├── campushub.db
├── requirements.txt
└── README.md
```

## 10. Deliverables

- SQLite database with sample data
- JSON import and export files
- Generated text reports
- Application log file
- Unit test files
- REST API documentation

