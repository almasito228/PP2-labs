# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#A tuple is a collection which is ordered and unchangeable.

#Tuples are written with round brackets.
#1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#3 Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#4 Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#5
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#6 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)