""" What does a map function do?: The map() function executes a specified function 
for each item in an iterable. 
The item is sent to the function as a parameter."""


list_int = [1, 12, 15, 21, 131]

list_string = map(str, list_int)

print(list(list_string))

list_char = ['a','b','c','d']

list_char = map(ord, list_char)

print(list(list_char))