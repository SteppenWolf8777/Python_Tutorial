class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)


class Person2:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person2("Emil")
p2 = Person2("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)



class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name}")

# Создаём объект p1 класса Person с именем "John" и возрастом 36
p1 = Person3("John", 36)

# Вызываем метод greet на объекте p1
p1.greet()


# Create the Dog class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says Woof!")
# Create an object
d1 = Dog("Buddy", 3)
# Call the bark method
d1.bark()


class Person4:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printname(self):
    print(self.name)

  def greet(self):
      print(self.age)

p1 = Person4("Tobias", 25)
p2 = Person4("Linus", 36)
print(p1.name, p1.age)
print(p2.name, p2.age)


p1.printname()
p2.greet()


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()


class Person5:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person5("Tobias")
p1.welcome()


class Person6:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person6("Emil")
p2 = Person6("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


class Person7:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person7("Linus")
p2 = Person7("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)


