b_date = (21, "May", 2004)  # tuples are written with round brackets
print(b_date)

coordinates = (48.8584, 2.2945)
print(coordinates[1])  # tuples are ordered from 0

eiffel_tower = (48.8584, 2.2945)
##eiffel_tower[0] = 56.7581 this would be an error, tuples are immutable

scores = (7, 9, 9, 8, 9)
print(
    "# of 7:", scores.count(7)
)  # count() function used to calculate # of occurrences of an item in tuple
print("# of 9:", scores.count(9))
print("# of 2:", scores.count(2))
print(len(scores))
print(max(scores))
# winner = max(scores)
# print(winner)

points = (12, 14, 9, 10, 9)
for point in points:
    if point > 10:
        print(point, ": passed")


birthday_date = (12, "August", 1993)
day, month, year = birthday_date
print(day)
print(month)
print(year)

scores_2 = (98, 96, 91, 88, 64)
winner, *rest = scores_2
print(winner)
print(rest)

years = [2002, 2008, 1999]
years[1] = 2007
for year in years:
    print(year)

guests = {
    "Mery",
    "Anna",
    "Jonathan",
}  # sets are unordered collections with curly brackets
print(guests)
# print(guests[0]) this would be an error, can't be indexed or sliced

# adding 'Robert'
guests.add("Robert")

# removing 'Mery'
guests.remove("Mery")
print(guests)

# clears the set
guests.clear()

guests_2 = {"John", "Lee", "Tim"}
combined_set = guests.union(guests_2)  # combines the two guest sets
print(combined_set)

set1 = {"apple", "banana"}
set2 = {"orange", "cherry", "banana"}
unique = set1.difference(set2)  # returns values in first set, not the second
print(unique)

# dictionary
product = {
    "name": "pen",  # type:value
    "color": "red",
    "price": 79,
}

car = {  # dictionary name
    "brand": "Audi",  # keys are "brand" and "model"
    "model": "Q5",  # values are "Audi" and "Q5"
    "year": "2008",
}

print(car["brand"])
print(car["model"])
print(car["year"])

dancer = {__name__: "Maria", points: [8, 6, 10]}

print(dancer)

website = {
    "url": "Facebook",
    "search": "Google",
    "search": "Apple",  # displays Apple when printed
}

print(website)

contact = {
    "name": "John",
    "company": "Google",
}

info_keys = contact.keys()
info_values = contact.values()
info = car.items()

print(info_keys)
print(info_values)
print(info)

user = {"Name": "Albert", "Age": 29}
user["Age"] = 30

# update() fcuntion updates the dictionary with items from given argument
user.update({"Age": 31})

print(user["Age"])
print(user.items())

clock = {"Night": "Sleep", "Morning": "Wake up", "Afternoon": "Lunch"}

# removing the item with the "Afternoon" key
clock.pop("Afternoon")
print(car)

# checks if key or value occurs in dictionary
print("Night" in clock)
print("Sleep" in clock.values())

school = {"Supplies": "Pencils", "Classes": "Math"}

nums = []  # creates a list containing numbers from 1 to 50

for x in range(1, 100):
    nums.append(x)

    print(nums)

numbers = {x for x in range(1, 51)}  # shorcut for loops
print(numbers)
##<variable> = [<expression> for <item> in <iterable>]

numbers_1 = {x * 2 for x in range(10)}
# doubles each value in range(10)
print(numbers_1)

# this code goes through list of tags, adds # symbol behind them
tags = ["travel", "vacation", "journey"]

hashtags = ["#" + x for x in tags]
print(hashtags)

cities = ["madrid", "paris", "lisabon"]

cities_cap = [x.capitalize() for x in cities]
print(cities_cap)

# filters out names that start with "B"
users = ["Bradon", "Emma", "Brian"]

group = [x for x in users if x[0] == "B"]

print(group)

sports = ["Football", "Basketball", "Tennis", "Golf", "Volleyball"]
group_1 = [x for x in sports if "ball" in x]

print(group_1)

prices = [250, 300, 240, 400]
total = sum(prices)
print(total)

error = [250, 300, "240", 400]
try:
    # block that may cause an exception
    totals = sum(error)
    print(totals)

except TypeError:
    # to perform if there is an exception
    print("Invalid data type")

except NameError:  # you can have multiple except blocks
    print("Invalid variable")

except:  # you can also just use one except block
    print("Error")

finally:  # performs operation after try/except block
    print("Need help? Contact us")

print("Happy Shopping")

books = ["Harry Potter", "Dune", "Emma"]
try:
    choice = books[1]
except IndexError:
    print("Out of Range")
else:  # else is only executed when no errors occur in try block
    print(choice + " is a great choice")

##rating = 15
##if rating > 10 or rating <0:
# raise ValueError("Rate from 0 to 10") #creates own exception


def welcome(name):
    return "Welcome, " + name


greet = welcome
print(greet("Bob"))


def order(dish):
    return "Your order: " + dish


def process_order(dish, func):  # higher order function
    print(func(dish))


process_order("Spaghetti", order)


def book_title(title):
    return "Book title: " + title


def info(title, func):
    return func(title)


print(info("The Great Gatsby", book_title))


def welcome_1(user):
    print("Welcome,", user)  # impure function, modified externally


def pure(num1, num2):
    y = (num1 * num2) / num2  # pure function, same output everytime
    return y


print(pure(12, 45))

# lambda expressions are efficient features in python that allow you to create compact and throwaway functions without a formal structure or definition

lambda x: x + 5  # lambda <argument>: <expression>

print(x)

x = lambda price, count: price * count
print(x(2, 10))

res = (lambda x, y: x * y)(2, 3)

price_2 = [25.99, 14.50, 8.75, 19.95]


def discount(price_2):
    discounted_price = price_2 * 0.9
    return discounted_price


discounted_prices = list(map(discount, price_2))

exam_scores = [85, 62, 95]


def is_passing(score):
    return score >= 70


status = list(map(is_passing, exam_scores))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))  # executes specified function for each item in an iterable


def myfunc(a, b):
    return a + b


x = map(myfunc, ("apple", "banana", "cherry"), ("orange", "lemon", "pineapple"))

print(x)

# convert the map into a list, for readability:
print(list(x))


names = ["John", "Emma", "Jake", "Rachel", "James"]
filtered = list(
    filter(lambda name: name[0] == "J", names)
)  # useful for extracting subsets of data that meet certain criteria


def my_function(*kids):  # * used when # of arguments is unknown
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def display(*words):
    for item in words:
        print(item)


display("paper", "pen", "pencil")


def my_kwarg(**kid):
    print("His last name is " + kid["lname"])


my_kwarg(fname="Tobias", lname="Refsnes")


def order():
    def prepare():
        return "Your meal is being prepared!"

    status = prepare()
    return status


order()

# classes are the blueprints
# objects are the instances


class Person:  # you can define a class by using the class keyword, followed by name and colon
    def __init__(self, name, age):  # init function assigns values to object properties
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class my_Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


Car = my_Car("Toyota", "green")  # instance

print(Car.brand)


class Audi:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def greeting(self):  # Function, called methods include 'self' parameter
        print("I'm a Q5")


my_Audi = Audi("Q5", "yellow")

my_Audi.greeting()


# Inheritance
class Animal:  # Parent Class
    def __init__(self, name) -> None:
        pass
        self.name = name

    def move(self):
        print("Moving")

    # Generic sound method for any animal
    def sound(self):
        print("Making a sound")


# Inherits from Animal class
class Dog(Animal):  # Child Class
    def __init__(self, name, breed, age) -> None:
        super().__init__(
            name
        )  # super __init__() is used to inherit attributes from parent class
        self.breed = breed
        self.age = age

    # Specific method
    def bark(self):
        print("Woof")

    # Overidden sound method for Dog
    def sound(self):
        super().sound()  # Super function calls methods from parent class while overriding it, adds functionality to the new without changing the original method
        print("Barking")


class Cat(Animal):
    def __init__(self, name, breed, age) -> None:
        super().__init__(name)
        self.breed = breed
        self.age = age

    def sound(self):
        print("Meowing")


# Creating an instance
my_dog = Dog("Bob", "Bulldog", 7)
my_cat = Cat("Whiskers", "Ragdoll", 5)

# Inherited attributes and behaviors
print(my_dog.name)
print(my_dog.breed)
print(my_dog.age)
print(my_cat.name)
my_dog.move()

# Specific method
my_dog.bark()
# my_cat.sound()
# my_dog.sound()

animals = [
    my_dog,
    my_cat,
]  # Polymorphism lets objects used methods no matter their subclass

# Plays dog and cat sounds
for animal in animals:
    animal.sound()


class Person:
    def __init__(self, name, age) -> None:
        pass
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, faculty) -> None:
        super().__init__(name, age)
        self.faculty = faculty


my_Student = Student("Max", "15", "Not Faculty")

print(my_Student.faculty)

# Data Hiding,
# Prevents attribute from being changed, in this case the odometer


class Meter:
    def __init__(self, model, year, odometer) -> None:
        pass
        self.model = model
        self.year = year
        # Making the odometer attribute 'protected' by putting an '_'
        self._odometer = odometer

    def describe_meter(self):
        print(self.year, self.model)

    def read_odometer(self):
        print(
            "Odometer", self._odometer, "miles"
        )  # Underscores make them accessible, but considered protected, should be used cautiously outside the class


my_Meter = Meter("Luxury", "2020", "15000")

# Accesing protected attribute, use the '_' when calling it
print(my_Meter._odometer)

my_Meter.describe_meter()
my_Meter.read_odometer()


class Cars:
    def __init__(self, model, year, odometer):
        self.model = model
        self.year = year
        # Making the odometer attribute 'private' using two underscores, '__', used for sensitive or internal data, discouraging external access
        self.__odometer = odometer

    def describe_car(self):
        print(self.year, self.model)

    def read_odometer(self):
        print("Odometer", self.__odometer, "miles")


my_car = Cars("BMW", 2020, 20000)

# Accesing using name mangling
# print(my_car.Cars__odometer)

# Error
# my_car.read_odometer()

# Error
# print(my_car.__odometer)


class Book:
    def __init__(self, title, author) -> None:
        pass
        self.title = title
        self.author = author

        # Regular Method

    def describe_book(self):
        print(self.title, "by", self.author)

    # Class Method call on the class itself, not on instances.
    # Can be used without a class instance, useful for actions relevant to the whole class
    @classmethod
    def books_in_series(cls, series_name, number_of_books):
        print("There are", number_of_books, "books in the", series_name, "series")

    # Static Method doesn't use cls parameter
    # Can't access or modify class's state, useful for tasks that don't rely on knowledge of the class or instance
    @staticmethod
    def book_rating(series_name, number_of_books):
        print("The best", series_name, "book is book number", number_of_books)

        # Creating an instance of Book


my_book = Book("Harry Potter", "J.K Rowling")

# Using instance method to describe book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)

Book.book_rating("Harry Potter", 7)
