import curses.ascii


def outer(name):
    def inner():
        print( f"Hello, {name}!")
    return inner

def create(s):
    return lambda x: x == s


def create_account(user_name, password, secret_words):
    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long")

    has_up = any(char.isupper() for char in password)
    has_low = any(char.islower() for char in password)
    has_dig = any(char.isdigit() for char in password)
    has_sp = any(char in "!:;.,&?/|\\][{}-@#$%^&*()_+" for char in password)

    if not (has_up and has_low and has_dig and has_sp):
        raise ValueError(
            "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character")

    from collections import Counter

    def check(input_password, input_secret_words):
        if input_password != password:
            return False

        if len(input_secret_words) != len(secret_words):
            return False

        c_orig = Counter(secret_words)
        c_inp = Counter(input_secret_words)
        matches = sum(min(c_orig[k], c_inp[k]) for k in set(c_orig) | set(c_inp))
        mismatches = len(secret_words) - matches
        return mismatches <= 1

    return check

def divisor(num):
    for d in range(1, num + 1):
        if num % d == 0:
            yield d
    while True:
        yield None

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        parts = [str(a) for a in args]
        parts.extend(str(v) for v in kwargs.values())
        print(f"Executing of function {func.__name__} with arguments {', '.join(parts)}...")
        return result
    return wrapper

@logger
def concat(*args, **kwargs):
    parts = [str(a) for a in args]
    parts.extend(str(v) for v in kwargs.values())
    return ''.join(parts)

def randomWord(words):
    import random
    if not words:
        while True:
            yield None
    pool = list(words)
    random.shuffle(pool)
    i = 0
    while True:
        yield pool[i]
        i += 1
        if i >= len(pool):
            prev = pool
            pool = list(words)
            if len(pool) > 1:
                random.shuffle(pool)
                while pool == prev:
                    random.shuffle(pool)
            i = 0


# class Employee:
#     def __init__(self,firstname,lastname,salary):
#         self.firstname = str(firstname)
#         self.lastname = str(lastname)
#         self.salary = int(salary)
#
#     @staticmethod
#     def from_string(s):
#         parts = s.split("-")
#         first,last,sal = parts
#         return Employee(first,last,int(sal))

class Pizza:
    _order_counter = 0

    def __init__(self,ingredients):
        Pizza._order_counter += 1
        self.order_number = Pizza._order_counter
        self.ingredients = list(ingredients)

    @classmethod
    def garden_feast(cls):
        return cls(["spinach", "olives", "mushroom"])

    @classmethod
    def hawaiian(cls):
        return cls(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return cls(["beef", "meatball", "bacon"])

class Employee:
    def __init__(self,name,**kwargs):
        self.name = name
        parts = self.name.split()
        self.name,self.lastname = parts
        for key,value in kwargs.items():
            setattr(self,key,value)




class Testpaper:
    def __init__(self,subject,markscheme,pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark

class Student:
    def __init__(self):
        self.tests_taken = "No tests taken"

    def take_test(self,testpaper,answear):
        correct = sum(1 for c,a in zip(testpaper.markscheme,answear) if c == a)
        total = len(testpaper.markscheme)
        percentage = round((correct/total)*100)

        required = int(testpaper.pass_mark.strip().rstrip('%'))

        result_str = f"Passed! ({percentage}%)" if percentage >= required else f"Failed! ({percentage}%)"

        if self.tests_taken == "No tests taken":
            self.tests_taken = {}

        self.tests_taken[testpaper.subject] = result_str

class Gallows:
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self,word):
        if self.game_over:
            return "game over"

        if not isinstance(word,str) or len(word) == 0:
            self.game_over = True
            return "game over"

        if word in self.words:
            self.game_over = True
            return "game over"

        if self.words:
            last_char = self.words[-1][-1].lower()
            first_char = word[0].lower()
            if first_char != last_char:
                self.game_over = True
                return "game over"

        self.words.append(word)
        return self.words

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"



class Book:
    def __init__(self, title, author, year, quantity=1):
        self.title = title
        self.author = author
        self.year = int(year)
        self.quantity = max(0, int(quantity))

    def display_info(self):
        print(f"Book: '{self.title}' by {self.author} ({self.year}) - Copies: {self.quantity}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Quantity: {self.quantity}"


class EBook(Book):
    def __init__(self, title, author, year, format_type: str = "PDF", quantity= 1):
        super().__init__(title, author, year, quantity)
        self.format_type = format_type

    def display_info(self):
        print(
            f"EBook: '{self.title}' by {self.author} ({self.year}) - Format: {self.format_type} - Copies: {self.quantity}"
        )

    def __str__(self):
        base = super().__str__()
        return f"{base} Format: {self.format_type}"



class Library:
    def __init__(self):
        self.books: list[Book] = []
        self.book_count = 0

    def _find_index_by_identity(self, title, author, year):
        t, a, y = title.strip().lower(), author.strip().lower(), int(year)
        for idx, b in enumerate(self.books):
            if b.title.strip().lower() == t and b.author.strip().lower() == a and int(b.year) == y:
                return idx
        return None

    def find_book_by_title(self, title):
        t = title.strip().lower()
        for b in self.books:
            if b.title.strip().lower() == t:
                return b
        return None

    def add_book(self, book: Book):
        idx = self._find_index_by_identity(book.title, book.author, book.year)
        if idx is not None:
            self.books[idx].quantity += int(book.quantity)
        else:
            self.books.append(book)
        self.book_count += int(book.quantity)

    def display_books(self):
        if not self.books:
            print("Library has no books.")
            return
        print("Books in the Library:")
        for b in self.books:
            print(str(b))

class Customer:
    def __init__(self, name):
        self.name = name
        self.borrowed_books: list[Book] = []

    def __str__(self):
        return f"{self.name} borrowed books:{self.borrowed_books}"

    def borrow_book(self, arg1, title=None):
        if isinstance(arg1, Library):
            library = arg1
            if not isinstance(title, str) or not title.strip():
                print(f"{self.name}: invalid title.")
                return False
            book = library.find_book_by_title(title)
            if book is None:
                print(f"{self.name}: '{title}' not found in library.")
                return False
            if book.quantity <= 0:
                print(f"{self.name}: '{book.title}' is currently unavailable.")
                return False
            book.quantity -= 1
            library.book_count -= 1
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
            return True

        book = arg1
        if not isinstance(book, Book):
            print(f"{self.name}: invalid book reference.")
            return False
        if book.quantity <= 0:
            print(f"{self.name}: '{book.title}' is currently unavailable.")
            return False
        book.quantity -= 1
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")
        return True

    def return_book(self, arg1, title=None):
        if isinstance(arg1, Library):
            library = arg1
            if not isinstance(title, str) or not title.strip():
                print(f"{self.name}: invalid title.")
                return False
            idx = next((i for i, b in enumerate(self.borrowed_books)
                        if b.title.strip().lower() == title.strip().lower()), None)
            if idx is None:
                print(f"{self.name}: You have not borrowed '{title}'.")
                return False
            book = self.borrowed_books.pop(idx)
            lib_idx = library._find_index_by_identity(book.title, book.author, book.year)
            if lib_idx is None:
                library.books.append(Book(book.title, book.author, book.year, quantity=1))
            else:
                library.books[lib_idx].quantity += 1
            library.book_count += 1
            print(f"{self.name} returned '{book.title}'.")
            return True

        book = arg1
        if not isinstance(book, Book):
            print(f"{self.name}: invalid book reference.")
            return False
        try:
            self.borrowed_books.remove(book)
        except ValueError:
            print(f"{self.name}: You have not borrowed '{book.title}'.")
            return False
        book.quantity += 1
        print(f"{self.name} returned '{book.title}'.")
        return True

class LibraryManagementSystem:
    def __init__(self, library: Library | None = None):
        self.library = library if library is not None else Library()
        self.customers: list[Customer] = []

    def register_customer(self, customer: Customer):
        if any(c.name.strip().lower() == customer.name.strip().lower() for c in self.customers):
            print(f"Customer {customer.name} is already registered in the system.")
            return
        self.customers.append(customer)
        print(f"Customer {customer.name} registered in the system.")

    def _get_customer(self, name_or_customer):
        if isinstance(name_or_customer, Customer):
            n = name_or_customer.name.strip().lower()
        else:
            n = str(name_or_customer).strip().lower()
        for c in self.customers:
            if c.name.strip().lower() == n:
                return c
        return None

    def display_customer_books(self, customer_name_or_obj):
        customer = self._get_customer(customer_name_or_obj)
        if customer is None:
            print(f"Customer '{customer_name_or_obj}' not found.")
            return
        print(f"Books borrowed by {customer.name}:")
        for b in customer.borrowed_books:
            print(str(b))

    def display_all_books(self):
        self.library.display_books()

from functools import total_ordering
from typing import Iterable, Callable

@total_ordering
class Task:
    def __init__(self, title: str, priority: int, tags: Iterable[str] | None = None, done: bool = False):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        if not isinstance(priority, int) or priority < 0:
            raise ValueError("priority must be a non-negative int")
        self.title = title.strip()
        self.priority = priority
        self.tags = tuple((t or "").strip() for t in (tags or ()))
        self.done = bool(done)

    def __str__(self):
        status = "done" if self.done else "open"
        tags = ", ".join(self.tags) if self.tags else "-"
        return f"Task '{this.title}' (priority={self.priority}, status={status}, tags=[{tags}])"

    def __repr__(self):
        return f"Task(title={self.title!r}, priority={self.priority!r}, tags={self.tags!r}, done={self.done!r})"

    def __eq__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return (self.title, self.priority, self.tags, self.done) == (other.title, other.priority, other.tags, other.done)

    def __lt__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return (self.priority, self.title) < (other.priority, other.title)

    def __hash__(self):
        return hash((self.title, self.priority, self.tags, self.done))

    def mark_done(self):
        self.done = True
        return self

    def add_tag(self, tag: str):
        tag = (tag or "").strip()
        if not tag:
            return self
        if tag not in self.tags:
            self.tags = tuple(list(self.tags) + [tag])
        return self

    def remove_tag(self, tag: str):
        tag = (tag or "").strip()
        if not tag:
            return self
        self.tags = tuple(t for t in self.tags if t != tag)
        return self

    def as_dict(self, key_transform: Callable[[str], str] = lambda k: k):
        base = {
            "title": self.title,
            "priority": self.priority,
            "tags": list(self.tags),
            "done": self.done,
        }
        return {key_transform(k): v for k, v in base.items()}

    @staticmethod
    def from_string(s: str):
        parts = [p.strip() for p in (s or "").split("|")]
        if len(parts) < 2:
            raise ValueError("format: 'title | priority | [tags] | [done]'")
        title = parts[0]
        priority = int(parts[1])
        tags = []
        done = False
        if len(parts) >= 3 and parts[2]:
            tags = [t.strip() for t in parts[2].split(",") if t.strip()]
        if len(parts) >= 4 and parts[3]:
            done = parts[3].lower() in ("1", "true", "yes", "y")
        return Task(title, priority, tags, done)



















    import logging

    logging.

    def average(numbers):

    # type your code here

    average([1, 2, 3, 4, 5])
    average([10, -20, -30])
    average([])
    average([1, 2, 3, 0, 5])
    average([1, 2, "three", 4, 5])