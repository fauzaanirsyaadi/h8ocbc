# create file
f = open('sesi4.txt', 'w')
f.write('ini adalah file baru')
f.close()

print()
# open file
f = open('sesi4.txt', 'r')

print()
# read file
print(f.read())

print()
# close file
f.close()

print()
# write file
f = open('sesi4.txt', 'w')
f.write('ini adalah file baru')
f.close()

print()
# append file
f = open('sesi4.txt', 'a')
f.write('\nini adalah file baru')
f.close()

print()
# read file
f = open('sesi4.txt', 'r')
print(f.read())
f.close()

print()
# read file
f = open('sesi4.txt', 'r')
print(f.read(5))
f.close()

print()
# read file
f = open('sesi4.txt', 'r')
print(f.readline())
f.close()

print()
# override file
f = open('sesi4.txt', 'w')
f.write('ini adalah file baru')
f.close()

# tell file
f = open('sesi4.txt', 'r')
print(f.tell())
f.close()

# seek file
f = open('sesi4.txt', 'r')
f.seek(5)
print(f.read())
f.close()

# remove file
# import os
# os.remove('sesi4.txt')

print()
# try and except block
try:
    f = open('sesi4.txt', 'r')
    print(f.read())
except:
    print('file tidak ditemukan')
    f.close()

print()
# try else clause
try:
    f = open('sesi4.txt', 'r')
    print(f.read())
except:
    print('file tidak ditemukan')
else:
    print('file ditemukan')
    f.close()

print()
# try and catch with finally
try:
    f = open('sesi4.txt', 'r')
    print(f.read())
except:
    print('file tidak ditemukan')
finally:
    print('file ditemukan')
    f.close()

print()
# buffer file
f = open('sesi4.txt', 'r')
print(f.read(5))

print()
# raw file types
f = open('sesi4.txt', 'rb')
print(f.read())
f.close()

print()
# buffered binary file types
f = open('sesi4.txt', 'rb')
print(f.read(5))
f.close()

print()
# assertion error except
try:
    assert False
except AssertionError:
    print('assertion error')

print()
# try and except blocked
try:
    assert False
except AssertionError:
    print('assertion error')
else:
    print('assertion error')

print()
#  cleaning up after useing finally
try:
    f = open('sesi4.txt', 'r')
    print(f.read())
except:
    print('file tidak ditemukan')
finally:
    print('file ditemukan')
    f.close()

print()


#  check coin with assert
def check_coin(coin):
    assert coin in ['bitcoin', 'ethereum', 'ripple'], 'invalid coin'
    print('valid coin')


print(check_coin('bitcoin'))
print(check_coin('ethereum'))
print(check_coin('ripple'))
print(check_coin('bitcoin'))

print()


# assert equal
def check_equal(a, b):
    assert a == b, 'not equal'
    print('equal')


# print(check_equal(1, 1))
# print(check_equal(1, 2))

# unit test sum
print('unit test')


def add(a, b):
    return a + b


def test_sum():
    assert add(1, 2) == 3
    assert add(1, 2) == 4


# print(test_sum())

print()


# match function with case
def match(a, b):
    if a == b:
        return True
    else:
        return False


print(match(1, 1))

print()


# case function
def case(a):
    if a == 1:
        return 'one'
    elif a == 2:
        return 'two'
    else:
        return 'other'


print(case(1))
print(case(2))
print(case(3))

print('\nenums')


# enum function class color and print
class Color:
    RED = 1
    GREEN = 2
    BLUE = 3


def print_color(self):
    print(self.RED)
    print(self.GREEN)
    print(self.BLUE)


print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)
print_color(Color)

print('\ncalculator')


# switch case calculator
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return 'invalid operator'


print(calculator(1, 2, '+'))
print(calculator(1, 2, '-'))
print(calculator(1, 2, '*'))
print(calculator(1, 2, '/'))

# raise exception
print('\nraise exception')


def raise_exception(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'invalid divisor'


print(raise_exception(1, 1))

# raise
print('\nraise')


def raise_exception(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise


print(raise_exception(1, 0))

# chaining
print('\nchaining')


def raise_exception(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise
    except TypeError:
        return 'invalid type'


print(raise_exception(1, 0))


# user defined exception
print('\nuser defined exception')
