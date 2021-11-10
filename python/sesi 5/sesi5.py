# object oriented programming
# define a class of employee
class Employee:
    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # method
    def print_salary(self):
        print("{}'s salary is {}".format(self.name, self.salary))

    # instance method
    def increase_salary(self, increase):
        self.salary += increase
        print("{}'s salary is {}".format(self.name, self.salary))


# create an object of employee
employee1 = Employee("John", 200000)
# use print_salary to print
employee1.print_salary()
# use increase_salary to print
employee1.increase_salary(100000)

print('---')


# dog class method
class Dog:
    # class attributes
    species = 'mammal'

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def bark(self):
        print("{} is {} years old".format(self.name, self.age))

    #  instance method
    def eat(self):
        print("{} is eating".format(self.name))

    # instance method
    def sleep(self):
        print("{} is sleeping".format(self.name))

    # use attribute species in method
    def get_species(self):
        #         return name, age, and species
        return "{} is {} years old and {}".format(self.name, self.age, self.species)

    # dog speak whit input from object
    def speak(self, sound):
        print("{} is {}".format(self.name, sound))


# create object of dog
dog1 = Dog("Fido", 3)
# use bark to print
dog1.bark()
# use eat to print
dog1.eat()
# use sleep to print
dog1.sleep()
# use get_species
print(dog1.get_species())
# use speak to print
dog1.speak("woof")

print('---')


# inheritance class
class Animal:
    def __init__(self, name):
        # super classes
        self.name = name

    def speak(self):
        print("{} is speaking".format(self.name))

    def eat(self):
        print("{} is eating".format(self.name))

    def sleep(self):
        print("{} is sleeping".format(self.name))

    def run(self):
        print("{} is running".format(self.name))

print("---")
# inharitance sub class
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print("{} is running".format(self.name))

    def bark(self):
        print("{} is barking".format(self.name))

print("---")
# inharitance sub class
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def run(self):
        print("{} is running".format(self.name))

    def meow(self):
        print("{} is meowing".format(self.name))


# call inharitance animal and sub class
animal1 = Animal("animal1")
animal1.speak()
animal1.eat()
animal1.sleep()
animal1.run()

# sub class
dog1 = Dog("dog1")
dog1.speak()
dog1.eat()
dog1.sleep()

# sub class
cat1 = Cat("cat1")
cat1.speak()
cat1.eat()
cat1.sleep()
cat1.run()

print("---")
# super user class example
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self):
        print("{} is logged in".format(self.name))

    def logout(self):
        print("{} is logged out".format(self.name))

    def show_user_info(self):
        print("{}'s email is {} and password is {}".format(self.name, self.email, self.password))

    def change_password(self, new_password):
        self.password = new_password
        print("{}'s password is changed to {}".format(self.name, self.password))

    def change_email(self, new_email):
        self.email = new_email
        print("{}'s email is changed to {}".format(self.name, self.email))

    def delete_account(self):
        self.name = None
        self.email = None
        self.password = None
        print("{}'s account is deleted".format(self.name))


# create object of user
user1 = User("John", "john@email.com", "12345")
# use login to print
user1.login()
# use show_user_info to print
user1.show_user_info()
# use change_password to print
user1.change_password("123456")
# use change_email to print
user1.change_email("email@john.com")
# use delete_account to print
user1.delete_account()

print("---")
# parent and children class example for book
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("{} is deleted".format(self.title))

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __truediv__(self, other):
        return self.pages / other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __ne__(self, other):
        return self.pages != other.pages

    def __iadd__(self, other):
        self.pages += other.pages
        return self.pages

    def __isub__(self, other):
        self.pages -= other.pages
        return self.pages

    def __imul__(self, other):
        self.pages *= other.pages
        return self.pages

    def __itruediv__(self, other):
        self.pages /= other.pages
        return self.pages

    def __ifloordiv__(self, other):
        self.pages //= other.pages
        return self.pages

    def __imod__(self, other):
        self.pages %= other.pages
        return self.pages

    def __ipow__(self, other):
        self.pages **= other.pages
        return self.pages

    def __ilshift__(self, other):
        self.pages <<= other.pages
        return self.pages

    def __irshift__(self, other):
        self.pages >>= other.pages
        return self.pages

    def __iand__(self, other):
        self.pages &= other.pages
        return self.pages

    def __ixor__(self, other):
        self.pages ^= other.pages
        return self.pages

    def __ior__(self, other):
        self.pages |= other.pages
        return self.pages

    def __neg__(self):
        return -self.pages

    def __pos__(self):
        return +self.pages

    def __abs__(self):
        return abs(self.pages)

    def __invert__(self):
        return ~self.pages

    def __round__(self):
        return round(self.pages)


# create object of all book classes
book1 = Book("Python", "John", 200)
# use str to print
print(book1)
# use len to print
print(len(book1))
# use del to print
del book1

book1 = Book("Python", "John", 200)
book2 = Book("Java", "John", 300)

# use add to print
print(book1 + book1)
# use sub to print
print(book1 - book1)
# use mul to print
print(book1 * book1)
# use div to print
print(book1 / book1)
# use lt to print
print(book1 < book1)
# use gt to print
print(book1 > book1)
# use eq to print
print(book1 == book1)
# use le to print
print(book1 <= book1)
# use ge to print
print(book1 >= book1)
# use ne to print
print(book1 != book1)
# use iadd to print
book1 += book1
print(book1)
# use isub to print
book1 -= book1
print(book1)
# use imul to print
book1 *= book1
print(book1)
# use itruediv to print
# book1 /= book1
# print(book1)
# use ifloordiv to print
book1 //= book1
print(book1)
# use imod to print
book1 %= book1
print(book1)
# use ipow to print
book1 **= book1
print(book1)
# use ilshift to print
book1 <<= book1
print(book1)
# use irshift to print
book1 >>= book1
print(book1)
# use iand to print
book1 &= book1
print(book1)
# use ixor to print
book1 ^= book1
print(book1)
# use ior to print
book1 |= book1
print(book1)
# use neg to print
print(-book1)
# use pos to print
print(+book1)
# use abs to print
print(abs(book1))
# use invert to print
print(~book1)
# use round to print
print(round(book1))
