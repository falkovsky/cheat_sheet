# Tuples operations and methods

# Create empty tuple
my_tuple = ()
print(type(my_tuple))
# <class 'tuple'>

t = (1,2,'text', True, 100500, 'more text')
t2 = (9,8,7,'text')

print(t)
# (1, 2, 'text', True, 100500, 'more text')

print(t2)
# (9, 8, 7, 'text')

# Add element to tuple
t2 += (10,)
print(t2)
# (9, 8, 7, 'text', 10)

# Concatenate Tuples
t = t + t2
print(t)
# (1, 2, 'text', True, 100500, 'more text', 9, 8, 7, 'text', 10)

# Splits string by a separator value and maxsplit times
str.split(sep=None, maxsplit=1)

str_sys = '/bin:/usr/bin:/usr/local/bin'
str_sys.split(sep=':')
# ['/bin', '/usr/bin', '/usr/local/bin']

# Example of check for non-text elements:
for i in t:
	if not isinstance(i, str):
		print(i)
# 1
# 2
# True
# 100500
# 9
# 8
# 7
# 10

# LISTS operations and methods

# Create empty list:
l = []
print(type(l))
# <class 'list'>

l = [1, 2, 5, 'text', False, 100]
print(l)
# [1, 2, 5, 'text', False, 100]
 
# Add element to list
l.append('more text')
print(l)
# [1, 2, 5, 'text', False, 100, 'more text']

# Delete last element from list:
l.pop()
'more text'
print(l)
# [1, 2, 5, 'text', False, 100]
 
# Print out deleted element from list:
popped = l.pop()
print(popped)
# 100
print(l)
# [1, 2, 5, 'text', False]

# Delete element from list with certain position:
print(l)
# [1, 2, 5, 'text', False]
l.pop(2)
print(l)
# [1, 2, 'text', False]

# Create list from range:
my_list = list(range(1,10))
print(my_list)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# DICTIONARIES operations and methods:

# Create empty dict
d = {}
print(type(d))
# <class 'dict'>

# Create dictionaty
d = {'first':'key', 2:'second key', 'third':'key'}
print(d)
# {'first': 'key', 2: 'second key', 'third': 'key'}

# Print value of second key
print(d[2])
# 'second key'

# Print value of third key
print(d['third'])
# 'key'

# Change (update) value of first key
d.update({'first':1})
print(d)
# {'first': 1, 2: 'second key', 'third': 'key'}

# Update value of second key
d[2] = 3
print(d)
# {'first': 1, 2: 3, 'third': 'key'}

# Update value of third key
d[3] = 3
print(d)
# {'first': 1, 2: 3, 'third': 'key', 3: 3}

# Add new unique element to dictionary
d.update({'new':'item'})
print(d)
# {'first': 1, 2: 3, 'third': 'key', 3: 3, 'new': 'item'}

d.update({2:4})
print(d)
# {'first': 1, 2: 4, 'third': 'key', 3: 3, 'new': 'item'}

# Get the key value from dict (get method will not give an error 
# if the key doesn't exist):
print(d.get(2))
# 4

# Print all keys from dict:
print(d.keys())
# dict_keys(['first', 2, 'third', 3, 'new'])

# Print all values from dict:
print(d.values())
# dict_values([1, 4, 'key', 3, 'item'])

# Get the length of the dict:
print(len(d))
5

# Iterate through dict:
for i in d:
    print(i)
# first
# 2
# third
# 3
# new

# Iterate through the dict and print both keys and values:
for key in d:
	print(key, d[key])
# first 1
# 2 4
# third key
# 3 3
# new item

# Or the same iteration:
for key, value in d.items():
	print(key, value)
# first 1
# 2 4
# third key
# 3 3
# new item

# Delete element from dict:
d.pop(3)
print(d)
# {'first': 1, 2: 4, 'third': 'key', 'new': 'item'}

popped = d.pop('new')
print(popped)
# item

# EXCEPTIONS

try:
	r = 1 / 0
except ValueError:
	print("Error happened")
except ZeroDivisionError:
	print('Can\'t divide for zero' )
except TypeError:
	print('Wrong type')

# =============================================

try:
	print(1 / 0)
except ZeroDivisionError as e:
	print('Exception! Can\'t divide!')
	print(e)

# Raise an exception and catch raised exception:

try:
	raise TypeError('Some error!')
except TypeError as e:
	print(e)

# ===============================================

try:
	print(1 / 0)
except ZeroDivisionError:
	print('0!')
finally:
	print('This will be executed anyway!')

# FUNCTIONS

# Function with two parameters:

def my_sum(a, b):
	res = a * b
	return res
x = my_sum(5, 3)
print(x)

# ====================================

def with_default(name='John'):
	print('Hello', name)

# =======================================

def with_few(pos, default_arg='some'):
	print(pos, default_arg)

# =======================================

# Function with args, non-limit:

def sum_all(*numbers):
	print(numbers, type(numbers))

print(sum_all(1, 8))
# (1, 8) <class 'tuple'>
# ------------------------------------
# Example:

def sum_all(*numbers):
	res = 0
	# print(numbers, type(numbers))
	for i in numbers:
		res = res + i
	return res

print(sum_all(1, 8, 12, 15, 2, 100))
# 138

# ======================================

# Function with keyword args (**kwargs):

def my_func2(**words):
  print(words, type(words))

my_func('one', 'two', 'three')
# ('one', 'two', 'three') <class 'tuple'>

def any_keywords(**kwargs):
	print(kwargs, type(kwargs))

any_keywords(first=1, second=2, third=3)
# {'first': 1, 'second': 2, 'third': 3} <class 'dict'>