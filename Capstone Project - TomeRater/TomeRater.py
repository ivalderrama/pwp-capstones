class User:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{}'s email has been updated".format(self.name))

    def __repr__(self):
        return "User: {}, Email: {}, Books read: {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_avg_rating(self):
        num_rating = 0

        for k, v in self.books.items():
            if v == None:
                v = 0
            else:
                num_rating += v

        return num_rating / len(self.books)


class Book:
    def __init__(self, title, isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{}'s ISBN has been updated to {}".format(self.title, self.isbn))

    def add_rating(self, rating):

        valid_rating = list(range(0, 5))

        if rating == None:
            rating = 0

        if rating in valid_rating:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __repr__(self):
        return "Book: {}, ISBN: {}".format(self.title, self.isbn)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_avg_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = str(subject)
        self.level = str(level)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)


class TomeRater:
    def __init__(self):
        self.users = {}  # Map user's email to user object, i.e {"test@test.com": Ivan}
        self.books = {}  # Map book object to number of users that have read it {test_fiction: 3}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):

        if email not in self.users:
            print("No user with email")
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)  # Need to fix this

        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1

    def add_user(self, name, email, books_list=None):
        self.users[email] = User(name, email)

        if books_list is not None:
            for i in books_list:
                self.add_book_to_user(i, email)

    def print_catalog(self):
        for k, v in self.books.items():
            print("Books: {}".format(k))

    def print_users(self):
        for k, v in self.users.items():
            print(v)

    def most_read_book(self):

        new_value = 0

        for k, v in self.books.items():
            if v > new_value:
                new_value = v

        for k, v in self.books.items():
            if new_value == v:
                return k

    def highest_rated_book(self):

        highest_rating = 0

        for k, v in self.books.items():
            if k.get_avg_rating() > highest_rating:
                highest_rating = k.get_avg_rating()

        for k, v in self.books.items():
            if highest_rating == k.get_avg_rating():
                return k

    def most_positive_user(self):
        highest_rating = 0

        for k, v in self.users.items():
            if v.get_avg_rating() > highest_rating:
                highest_rating = v.get_avg_rating()

        for k, v in self.users.items():
            if highest_rating == v.get_avg_rating():
                return v
