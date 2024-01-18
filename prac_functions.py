# make a function and call it
def greet():
    print("Hello Nadim")

greet()

# function with input values
# parameter and argument
# In below example name is parameter and the name what we give is argument

def greet_name(name):
    print(f"Hello {name}")

greet_name("Billu")
greet_name("Raju")

# function with 2 input values and keyword  arguments

def greet_2(name,location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}?")

greet_2(location="London",name="Nadim")



