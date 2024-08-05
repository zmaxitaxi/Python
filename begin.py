print("Hello World")

for i in range(100):
  print("Hello")

for i in range(10): #used when you do know how many loops you need
    print(i)

for i in range(5): #prints Max five times
    print("Max")

    seats = 30
while seats > 0: #used when you don't know how many loops you need
  print("Sell ticket")
  seats = seats - 1

  age = 30
if age >= 18: #conditional statement
  print("Regular price")
else:
  print("Discount")
print("Proceed to payment")

age = 16
if age < 18: print("Apply Discount")
print("Proceed to Payment")

if age < 18:
  print("Junior discount")
elif age >= 75:
  print("Senior discount")
else:
  print("No discount")

if age < 18:
  print("20% discount")
elif age>=60:
  print("10% discount")
else:
  print("Regular price")

cart = ["milk", "eggs", "apples"]

compositions = [
"Symphony No. 5",
"Symphony No. 3",
"Symphony No. 7"
]
print(compositions)

animals = [
  "dog",
  "bird",
  "cat"
]

print(animals[0])

products = ["apples", "oranges", "bananas"]
products[2] =  "lime" #can only change lists, not strings
print(products[2])

words = ["rise", "sun", "glasses"]
print(words[1] + words[0])

name = "Lee"
country = "France"
user_info = [name, country]
print(user_info[0])

products = ["juice", "chocolate", "water"]
user_choice = 1
print(products[user_choice])

notification = "New message!"
print(notification[4])

animals =['cat', 'dog', 'bird', 'cow']
print(animals[2:4])

animals =['cat', 'dog', 'bird', 'cow']
print(animals[1:4])

colors = ['red', 'green', 'blue', 'yellow']
print(colors[2:4])

colors = ['red', 'green', 'blue', 'yellow']
print(colors[2:3])

fruit = 'orange'
print(fruit[0:2])

color = 'pink'
print(color[1:4])

cart = ['lamp','candles', 'chair,', 'carpet']
print(cart[:2])

vehicle = 'motorbike'
print(vehicle[:5])

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[2:])

cart = ['lamp', 'candles', 'chair', 'carpet']
print(cart[1:])

vehicle = 'motorbike'
print(vehicle[5:])

vehicle = 'motorbike'
print(vehicle[:])

planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets[:])

char = ['A','B','C','D','E']
print(char[1:3])

planets = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets[:3])

c = ['$', '£', '€', '¥']
print(c[-1])

vehicle = 'motorbike'
print(vehicle[-1])

c = ['$', '£', '€', '¥']
print(c[-2:])

vehicle = 'motorbike'
print(vehicle[-4:])

c = ['$', '£', '€', '¥']
print(c[1:-1])

c = ['$', '£', '€', '¥']
print(c[0:-2])

c = ['$', '£', '€', '¥']
c[1] = '₣'
print(c)

c = ['$', '£', '€', '¥']
c[:2] = ['₣', '฿']
print(c)

brands = ["Honda", "Toyota", "BMW", "Mercedes"]
print(brands[-3:-1])

range(3) ##only takes integers

print("Your Seat:",4)

print(55*3)

x = "air"
y = "plane"
print(x + y)

number = 5
print("I have:", number)

print(type("word")) #type("word") is an argument of print

print(range(3))

num = '45' # string
print(int(num) + 3)

print("SMARTPHONE".lower())

brand = "ikea"
print(brand.upper())

print("christmas".capitalize())

print("Bee". find("e") ) #outputs postion of "e"

print("robot".find("o"))

print("robot".find("A"))

animals =['cat', 'dog', 'bird', 'cow']
print(len(animals))

movie = "Avatar"
print(len(movie))

c = ['$', '£', '€', '¥']
c.append("&")
print(c)

movies = ["Avatar", "Titanic", "Avengers"]
movies.append("Alien")
print(movies[3])

cart = ['lamp','candles', 'chair,', 'carpet']
cart.insert(2,'marker')
print(cart)
print(cart[2])

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green") #specific insert
colors.append("Black") #inserts at the end
print(colors[3])

products = ["apples", "oranges", "bananas"]
products.pop(1) #removes item from list
print(products)
print(products[1])

#function definition
def greet():
  print("hello".capitalize())
  print("have a good day".upper())

#function cal
greet()

def personal_greet(name): 
  print("Hello", name)
  print("Have a great day")

personal_greet("James")

print("Hello")

def bmi(weight, height):
    index = weight / (height * height)
    return index #sends value backx

patient_2 = bmi(5,8)#stores return value
print(bmi)

patient_3 = bmi(5,8)#stores return value
print("underweight", patient_3<18.5)


def convert_km(miles):
  kilometers = miles * 1.61
  return kilometers 
distance = (200)

km_1 = convert_km(20)
print(km_1)

def rect(length, width):
  area = length * width
  perimeter = 2* length + 2 * width
  return area, perimeter #2 values

x, y = rect(50,100) #2variables
print(x,y)

def profitable(d1,d2):
  area = d1 * d2 #numerical
  invest = area > 700 #boolean
  return invest

buy = profitable(90,120)
print(buy)

def rect(d1, d2):
  area = 0
  return area #ignores code after the return command
  area = d1 * d2

def greetings(name = "Guest"):
  print("Welcome", name)

greetings() #Welcome Guest
greetings("John") #Welcome John

word = 'motorbike'
print(word.find('r'))

book = "1984"
print(len(book))

movies=["Avatar","Titanic","Alien"]
movies.append("Avengers")
movies.insert(2, "Terminator")
print(movies[3])