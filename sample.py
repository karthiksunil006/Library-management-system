fiction_books = {
    "The Alchemist": {"author": "Paulo Coelho", "quantity": 3},
    "1984": {"author": "George Orwell", "quantity": 5},
    "To Kill a Mockingbird": {"author": "Harper Lee", "quantity": 4},
    "The Great Gatsby": {"author": "F. Scott Fitzgerald", "quantity": 2},
    "The Catcher in the Rye": {"author": "J.D. Salinger", "quantity": 3},
    "Brave New World": {"author": "Aldous Huxley", "quantity": 4},
    "Lord of the Flies": {"author": "William Golding", "quantity": 3},
    "Animal Farm": {"author": "George Orwell", "quantity": 5},
    "Pride and Prejudice": {"author": "Jane Austen", "quantity": 3},
    "The Old Man and the Sea": {"author": "Ernest Hemingway", "quantity": 4}
}

fiction_books["The Hobbit"] = {"author": "J.R.R. Tolkien", "quantity": 6}

for i in fiction_books:

    print(fiction_books[i]["author"])
    

