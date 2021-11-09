# build function example
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


# call a function
musuh = build_person('musuh', 'musuh', '20')
print(musuh)

print()


#  function arguments
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jessie')

print()


# required arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('hamster', 'harry')

print()


# keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')

print()


# default arguments
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('willie')

print()


# variable-length arguments
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


make_pizza('pepperoni', 'mushrooms', 'green peppers', 'extra cheese')

print()

print()


# length arguments with **
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value

    # for each key
    for key in profile:
        print(f"\nKey: {key}")

    # for each value
    for value in profile.values():
        print(f"\t{value}")

    return profile


print(build_profile('albert', 'einstein', location='princeton', field='physics'))


# The Anonymous Functions
# A function without a name is called an anonymous function.
# example of anonymous function:
def add_numbers(x, y):
    return x + y


# print anonymous function with lambda
print(lambda x, y: x + y)

print()

# return statements
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# print documentation for get_formatted_name
print(get_formatted_name.__doc__)

print()

print(get_formatted_name('jessie', 'musuh'))

print()


# scope of variables
# global and local variable
# global variable
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


# local variable scope
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# calculate rect
def get_rectangle_area(width, height):
    return width * height


# function of information
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


print()


# function of print information
def print_information(first_name, last_name):
    """Display information about a person."""
    print(f"\nHello, {first_name.title()} {last_name.title()}!")


# function variables length
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# function with items
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# pseudocode snippet implements an algorithm with smaller time complexity
# pseudocode snippet
def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate


# quick sort
def quick_sort(items):
    if len(items) <= 1:
        return items
