b_date = (21, 'May', 2004) #tuples are written with round brackets
print(b_date)

coordinates = (48.8584, 2.2945)
print(coordinates[1])#tuples are ordered from 0

eiffel_tower = (48.8584, 2.2945)
##eiffel_tower[0] = 56.7581 this would be an error, tuples are immutable

scores = (7, 9, 9, 8, 9)
print("# of 7:",scores.count(7)) #count() function used to calculate # of occurrences of an item in tuple
print("# of 9:",scores.count(9))
print("# of 2:",scores.count(2))
print(len(scores))
print(max(scores))
#winner = max(scores)
#print(winner)

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

guests = {"Mery", "Anna", "Jonathan"} #sets are unordered collections with curly brackets
print(guests) 
#print(guests[0]) this would be an error, can't be indexed or sliced

#adding 'Robert'
guests.add('Robert')

#removing 'Mery'
guests.remove('Mery')
print(guests)

#clears the set
guests.clear()

guests_2 = {'John', 'Lee', 'Tim'}
combined_set = guests.union(guests_2) #combines the two guest sets 
print(combined_set)

set1 = {'apple','banana'}
set2 = {'orange', 'cherry', 'banana'}
unique = set1.difference(set2) #returns values in first set, not the second
print(unique)

#dictionary
product = {
  "name": "pen", #type:value
  "color": "red",
  "price": 79
}

car = { #dictionary name
  "brand": "Audi", #keys are "brand" and "model"
  "model": "Q5", #values are "Audi" and "Q5"
  "year":"2008"
}

print(car["brand"])
print(car["model"])
print(car["year"])

dancer = {
  __name__: "Maria",  
  points: [8, 6, 10]
}

print(dancer)

website = {
  "url":"Facebook",
  "search":"Google",
  "search":"Apple" #displays Apple when printed
}

print(website)

contact = {
  "name":"John",
  "company":"Google",
}

info_keys = contact.keys()
info_values = contact.values()
info = car.items()

print(info_keys)
print(info_values)
print(info)

user = {
  "Name": "Albert",
  "Age":29
}
user["Age"] = 30

#update() fcuntion updates the dictionary with items from given argument
user.update({"Age":31})

print(user["Age"])
print(user.items())

clock = {
  "Night":"Sleep",
  "Morning":"Wake up",
  "Afternoon":"Lunch"
}

#removing the item with the "Afternoon" key
clock.pop("Afternoon")
print(car)

#checks if key or value occurs in dictionary
print("Night" in clock)
print("Sleep" in clock.values())

school = {
  "Supplies":"Pencils",
  "Classes":"Math"
}

for i in school:
  print(i) #returns keys

for i in school.values:
  print(i) #returns values














