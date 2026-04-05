def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")