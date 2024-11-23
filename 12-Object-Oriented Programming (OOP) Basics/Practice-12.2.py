class Book:
    def __init__(self, title, author):
        """
        Constructor to initialize the attributes of the Book object.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        print(f"Book '{self.title}' by {self.author} is created.")

    def __del__(self):
        """
        Destructor that prints a message when the object is destroyed.
        """
        print("The book is being destroyed!")

# Create a Book object
my_book = Book("1984", "George Orwell")

# Delete the Book object to trigger the destructor
del my_book
