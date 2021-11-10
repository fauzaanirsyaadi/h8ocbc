# me : halo copilot
# copilot : halo me


# example using generator
def gen_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# use generator
for i in gen_fibonacci(10):
    print(i)
print('---')


# example creating generator with 3 yield
# my generator
def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'


my_generator()

# use generator to print
for i in my_generator():
    print(i)
print('---')


# counter generator
def counter(n):
    for i in range(n):
        yield i


# use counter generator
for i in counter(10):
    print(i)
print('---')


# example from kode.id
def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1


for i in counter_generator(5, 10):
    print(i, end=' ')
    print()
print('---')

# first class object
print('first class object')


class MyClass:
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > 0:
            self.value -= 1
            return self.value
        else:
            raise StopIteration


# use first class object
for i in MyClass(10):
    print(i)
print('---')

# inner function
print('inner function')


def outer():
    print('outer function')

    def inner():
        print('inner function')

    inner()


# use inner function
outer()
print('---')


# use def inner
def outer2():
    print('outer 2 function')

    def inner():
        print('inner function')

    return inner


# use inner function
my_inner = outer2()
my_inner()
print('---')

# returning functions from functions
print('returning functions from functions')


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


# use returning functions from functions
print(parent(1)())
print(parent(2)())
print('---')

# returning functions from functions with parenthesized
print('returning functions from functions with parenthesized')


def parent2(num):
    def child():
        return num * num

    return child()


# use returning functions from functions with parenthesized
print(parent2(5))
print('---')

# simple decorator
print('simple decorator')


def decorator(func):
    def wrapper():
        print('before')
        func()
        print('after')

    return wrapper


@decorator
def say_hi():
    print('hi')


# use simple decorator
say_hi()
print('---')

# more example
print('more example')

import functools


def decorator_kode_id(func):
    print('decorator_kode_id')

    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        print('wrapper_decorator')
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


# use more example
@decorator_kode_id
def say_hi2():
    print('hi')


say_hi2()
print('---')

import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


# use timer
waste_some_time(1)
waste_some_time(10)
waste_some_time(999)
print('---')

# method overloading
print('method overloading')


class MyClass2:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MyClass2({self.value})'

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value

    def __lt__(self, other):
        return self.value < other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value


# use method overloading
a = MyClass2(10)
b = MyClass2(20)

print(a)
print(b)
print(a + b)
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print('---')


# example of dir class
print('example of dir class')


class MyClass3:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MyClass3({self.value})'

    def __dir__(self):
        return ['a', 'b', 'c']

    def __getattr__(self, item):
        if item == 'a':
            return self.value + 10
        elif item == 'b':
            return self.value + 20
        elif item == 'c':
            return self.value + 30
        else:
            raise AttributeError(f'{item} not found')


# use example of 2 dir class
a = MyClass3(10)
print(a.a)
print(a.b)
print(a.c)
print(dir(a))
print('---')