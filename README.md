 E-Learning Book Management System

This is a simple Book Management System built using Python for managing a small digital library. It allows users to add and view books through a command-line interface.

This project is ideal for beginners to understand basic file handling, JSON data storage, and menu-driven Python programs.

 Features

Add a Book: Enter the book title and author to save it to the collection.

View All Books: Display a list of all saved books with their titles and authors.

Data Persistence: All data is saved to a local JSON file (books.json) and loaded automatically when the program starts.

Technologies Used

Python 3

JSON (for storing book data)

Command-line Interface

 How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/e-learning-book-manager.git
cd e-learning-book-manager

2. Run the Program

Make sure you have Python installed. Then run:

python book_manager.py

3. Follow the On-Screen Menu
1. Add Book
2. View Books
3. Exit

 Project Structure
e-learning-book-manager/
│
├── book_manager.py     # Main Python script
├── books.json          # Auto-generated file to store book data
└── README.md           # Project documentation


SAMPLE OUTPUT:-

1. Add Book
2. View Books
3. Exit
Choice: 2
No books found.

1. Add Book
2. View Books
3. Exit
Choice: 1
Title: Harry Potter
Author: J.K. Rowling
Book added.

1. Add Book
2. View Books
3. Exit
Choice: 1
Title: The Alchemist
Author: Paulo Coelho
Book added.

1. Add Book
2. View Books
3. Exit
Choice: 2
1. Harry Potter by J.K. Rowling
2. The Alchemist by Paulo Coelho

1. Add Book
2. View Books
3. Exit
Choice: 3

[
    {"title": "Harry Potter", "author": "J.K. Rowling"},
    {"title": "The Alchemist", "author": "Paulo Coelho"}
]

