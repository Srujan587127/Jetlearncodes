textbook_dict = {
    'Physics': 250,
    'Math': 300,
    'Chemistry': 280
}

textbook_dict['Physics'] = 200
print("\nUpdated cost of Physics book.")

textbook_dict['Biology'] = 350
textbook_dict['English'] = 150
print("\nAdded two more books.")

book_name = input("\nEnter the name of the book to get its cost: ")
if book_name in textbook_dict:
    print(f"Cost of {book_name}: {textbook_dict[book_name]}")
else:
    print(f"{book_name} is not in the dictionary.")

print("All books and their costs:")
for book, cost in textbook_dict.items():
    print(f"{book}: {cost}")

print("Total number of books: {len(textbook_dict)}")
