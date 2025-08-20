import json
import os

FILE = 'books.json'

def load_books():
    if os.path.exists(FILE):
        with open(FILE, 'r') as f:
            return json.load(f)
    return []

def save_books(books):
    with open(FILE, 'w') as f:
        json.dump(books, f)

def add_book():
    title = input("Title: ")
    author = input("Author: ")
    books = load_books()
    books.append({'title': title, 'author': author})
    save_books(books)
    print("Book added.\n")

def view_books():
    books = load_books()
    if not books:
        print("No books found.\n")
    for i, book in enumerate(books, 1):
        print(f"{i}. {book['title']} by {book['author']}")
    print()

def menu():
    while True:
        print("1. Add Book\n2. View Books\n3. Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            break
        else:
            print("Invalid choice.\n")

menu()
