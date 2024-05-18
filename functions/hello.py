def hello(name):
    print("Hello {name}")


def year_of_birth(name,age):
    year = 2024-age
    print(f"Hello {name}, you were born in {year}")

def my_country(country="Uganda"):
    print(f"Hello AkiraChix from {country}")

def greet(*names):
    """greet"""
    for name in names:

        print(f"Hello {name}")

def add(x,y):
    sum = x+y
    return sum

def sum(*numbers):
    total = 0
    for number in numbers:
        total+=number
    return total


def multiplication(*numbers):
    total = 1
    for number in numbers:
        total*=number
    return total

def create_sentence(**words):
    sentence = ""
    for word in words.values():
        sentence  +=words
        sentence+= " "
        return sentence
    
def sum_and_greet(*args , **kwargs):
    total =0
    for x in args:
        total+=x
    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting = f"Hello{f} {l}  total of  your numbers is{total}"
    return greeting


