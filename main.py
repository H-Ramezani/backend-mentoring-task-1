import csv

import requests


API_URL = "https://openlibrary.org/search.json"
BOOKS_COUNT = 50
MIN_PUBLICATION_YEAR = 2000
OUTPUT_FILE = "books.csv"


def fetch_books():
    params = {
        "q": "python",
        "limit": BOOKS_COUNT,
    }

    response = requests.get(API_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data.get("docs", [])


def filter_books(books):
    filtered_books = []

    for book in books:
        year = book.get("first_publish_year")

        if year and year > MIN_PUBLICATION_YEAR:
            authors = book.get("author_name", [])

            filtered_books.append(
                {
                    "title": book.get("title", "Unknown"),
                    "authors": ", ".join(authors),
                    "year": year,
                }
            )

    return filtered_books


def save_to_csv(books):
    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "authors", "year"],
        )

        writer.writeheader()
        writer.writerows(books)


def main():
    books = fetch_books()
    filtered_books = filter_books(books)

    save_to_csv(filtered_books)

    print(f"Books fetched: {len(books)}")
    print(f"Books saved after filtering: {len(filtered_books)}")
    print(f"Output file: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()