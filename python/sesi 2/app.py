# the break and continue statements
# break : terminates the loop
# continue : skips the current iteration
n = 5
while n > 0:
    n -= 1
    if n == 2:
        # break
        continue
    print(n)
print("loop ended")

# if else example
# if condition:
#   statement(s)
# elif condition:
#   statement(s)
# else:
#   statement(s)

# ternary operator
# condition ? true : false
#  ternary operator example
#  x = 10
#  y = 20
#  x < y ? print("x is less than y") : print("x is greater than y")


# iteration example
# for x in range(10):
#   print(x)

# indefinitely iteration example
for x in range(10):
    print(x)
    if x == 5:
        break

#  while loop example
#  while condition:
#      statement(s)

print('while loop')
n = 5
while n > 0:
    n -= 1
    if n == 2:
        # break
        continue
    print(n)

#  for loop example
print('while loop condition')
counter = 0
while counter <= 10:
    print(counter)
    if counter ==3:
        break
    counter += 1

print()
i = 0
while i < 5:
    j = 0
    while j < 3:
        print(i, j)
        j += 1
        if j == 2:
            # break
            continue
        print('---')
        # j += 1
    i += 1

# while else example
# while condition:
#   statement(s)
# else:
#   statement(s)

# nested while loops
# while condition:
#   while condition:
#       statement(s)
#       if condition:
#           break
#       else:
#           continue
#   else:
#       statement(s)

print()
a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['foo', 'bar']
    while len(b):
        print(b.pop(0))
        if len(b) == 1:
            break
print()
#  one line while loop example in 10
x = 0
print(x)
x += 1
while x < 10:
    print(x)
    x += 1

#  while condition:
#      statement(s)

print()
# for loop example
x = 4
for x in range(0, 100, 20):
    print(x)

# range(start, stop, step)
# start : the starting value of the range
# stop : the ending value of the range
# step : the increment value of the range

print()
# altering for loop example
for x in range(10):
    print(x)
    if x == 5:
        break
    print('---')

# print index and value of dictionary
print()
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(key, ':', value)
print()
for key in d.keys():
    print(key)
print()
for value in d.values():
    print(value)
print()
for key in d:
    print(key)
    print(d[key])
    print('---')

# else Clause example
# while condition:
#   statement(s)
# else:
#   statement(s)

# else Clausein lists
print()
a = [1, 2, 3]
for x in a:
    print(x)
else:
    print('else')
