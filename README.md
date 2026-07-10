# Motivational Quotes App

A Django web application for displaying and managing motivational quotes and their authors.

The app stores quotes in a Django database and includes a custom management command to import quote data from a JSON file while preventing duplicate entries.

---

## Features

- Django-based web application
- Quote model with quote text and author fields
- SQLite database support
- Import quotes from JSON data
- Custom Django management command
- Duplicate quote prevention using `get_or_create()`
- Django admin support for managing quotes

---

## Tech Stack

- Python 3
- Django
- SQLite
- JSON data import

---

# Installation

## 1. Clone the repository

```bash
git clone <repository-url>
cd motivational-quotes-app
```
## 2. Create and activate a virtual environment

```bash
python3 -m venv env
```
- macOS/Linux
```bash
source env/bin/activate
```
- Windows
```bash
env\Scripts\activate
```
## 3. Install Dependencies
```bash
pip install Django
pip freeze > requirements.txt
```
## 4. Setup Database
```bash
python manage.py migrate
```
- This creates the database tables required by Django and the notable_quotes app

## 5. Loading Quotes into the Database
- Quotes are stored in
```
notable_quotes/
└── data/
    └── quotes.json
```
- The project includes a custom Django management command:
```
notable_quotes/
└── management/
    └── commands/
        └── load_quotes.py
```
```bash
python manage.py load_quotes
```
- The command:
    - Reads quotes from quotes.json
    - Creates database records
    - Skips quotes that already exist
    - Prevents duplicate entries using get_or_create()
- Example output:
```
Added: You were born an original, don't become a copy!
Added: Life is like riding a bicycle. To keep your balance, you must keep moving.
Skipped duplicate: Stay hungry, stay foolish.
```
## 6. Running the Application
- Start the Django development server:
```bash
python manage.py runserver
```
- Open:
```
http://127.0.0.1:8000/
```

# Django Admin (Optional)
### Create an admin user:
```bash
python manage.py createsuperuser
```
### Start the server
```bash
python manage.py runserver
```
### Open:
```
http://127.0.0.1:8000/admin/
```
- You can add, edit, and delete quotes through the Django admin interface.

# Project Structure
```
motivational-quotes-app/
│
├── manage.py
├── db.sqlite3
│
├── quotes/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── notable_quotes/
    ├── migrations/
    │   └── __init__.py
    │
    ├── management/
    │   └── commands/
    │       ├── __init__.py
    │       └── load_quotes.py
    │
    ├── data/
    │   └── quotes.json
    │
    ├── templates/
    │   └── notable_quotes/
    │
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    └── tests.py
```

## Licence
- This project is for learning and development purposes.
