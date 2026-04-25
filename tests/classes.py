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