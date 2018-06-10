# Tuples operations and methods

# create empty tuple
my_tuple = ()
print(type(my_tuple))
# <class 'tuple'>

t = (1,2,'text', True, 100500, 'more text')
t2 = (9,8,7,'text')

print(t)
# (1, 2, 'text', True, 100500, 'more text')

print(t2)
# (9, 8, 7, 'text')

# Adding element to tuple
t2 += (10,)
print(t2)
# (9, 8, 7, 'text', 10)

# Concatenating Tuples
t = t + t2
print(t)
# (1, 2, 'text', True, 100500, 'more text', 9, 8, 7, 'text', 10)

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

# Creating of empty list:
l = []
print(type(l))
# <class 'list'>

l = [1, 2, 5, 'text', False, 100]
print(l)
# [1, 2, 5, 'text', False, 100]
 
# Adding element to list
l.append('more text')
print(l)
# [1, 2, 5, 'text', False, 100, 'more text']

# Deleting of last element from list:
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

# Deleting element from list with certain position:
print(l)
# [1, 2, 5, 'text', False]
l.pop(2)
print(l)
# [1, 2, 'text', False]
