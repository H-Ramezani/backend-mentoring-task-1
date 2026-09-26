# Backend Mentoring - Task 1

A Python script that fetches 50 books from the OpenLibrary API, filters books published after 2000, and saves the results to a CSV file.

## Features

* Fetches 50 books from OpenLibrary.
* Filters books published after 2000.
* Extracts the book title, authors, and publication year.
* Saves the filtered results to `books.csv`.
* Uses a virtual environment for project dependencies.

## Requirements

* Python 3.10 or newer
* `requests`

## Installation

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install the required dependency:

```powershell
python -m pip install -r requirements.txt
```

## Run the Project

Run the following command:

```powershell
python main.py
```

The script will:

1. Fetch 50 books from OpenLibrary.
2. Keep books whose publication year is after 2000.
3. Save the filtered books to `books.csv`.

The terminal will show the number of fetched and saved books.

## Output

The generated CSV file contains the following columns:

* `title` — Book title
* `authors` — Author or authors
* `year` — First publication year

## Project Structure

```text
backend-mentoring-task-1/
│
├── .gitignore
├── README.md
├── books.csv
├── main.py
└── requirements.txt
```

## API

This project uses the OpenLibrary Search API:

`https://openlibrary.org/search.json`
