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