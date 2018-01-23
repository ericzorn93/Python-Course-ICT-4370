# Simple Example of an *Args function with many different arguments passed
def myArgs(*names):
    for count, name in enumerate(names):
        print(count, name)

myArgs("Bob", "Mary", "Sue", "Donny", "James", 22, 435.234, 2, "hello", "goodbye")


print("\n")


# Simple Example of a **Kwargs function with many different key-value pairs passed
def myKwargs(**days):
    for count, day in days.items():
        print(count, day)

# Function call with defined keys and values
myKwargs(
    first = "Sunday",
    second = "Monday",
    third = "Tuesday",
    fourth = "Wednesday",
    fifth = "Thursday",
    sixth = "Friday",
    seventh = "Saturday"
)

print("\n")

# Predefined Dictionary passed into the function using **kwargs
hello = {
    "first_name": "Eric",
    "last_name": "Zorn"
}

myKwargs(**hello)


# Creating a function using normal arg, *args, and **kwargs together
def together(name, *test1, **test2):
    print(name)
    for num, item in enumerate(test1):
        print(num, item)

    for num, second_item in enumerate(test2.values()):
        print(num, second_item)

# Predefined Variables
my_name = "John Smith"
ages = [22, 25, 18, 45, 83, 12, 24]
random_birthdays = {
    "first": "8/12/1992",
    "second": "9/25/1999",
    "third": "1/20/2018",
    "fourth": "6/15/2005"
}

print("\n")

# Together Function Call
together(my_name, *ages, **random_birthdays)





# Recursion Functions in Python
print("\nRecursive Function Calls\n-------------------")

def recursion(number):
    if number < 2:
        print(number)
        return number
    else:
        print(number)
        return number * recursion(number - 1)

# Recursion Function call will count down from 25 to 0
recursion(25)











# Question 2B
print("\n")

def sandwichToppings(*topping):
    toppings = []

    for item in topping:
        toppings.append(str(item).title())

    return toppings



first_sandwich = sandwichToppings("turkey", "lettuce", "mayo", "american cheese")
second_sandwich = sandwichToppings("chicken", "mozzarella cheese", "lettuce", "balsamic vinegar")
third_sandwich = sandwichToppings("grilled eggplant", "red peppers", "olive oil", "oregano")

print("First Sandwich: {0}".format(first_sandwich))
print("Second Sandwich: {0}".format(second_sandwich))
print("Third Sandwich: {0}".format(third_sandwich))

