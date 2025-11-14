# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Lists are part of the collections family in python
# Creating a list
my_list = [1, 2 , 3, 4, 5]
print(my_list) # [1, 2, 3, 4, 5]

print(len(my_list)) #5
print(type(my_list)) # <class 'list'>
print(my_list[0]) #1
print(my_list[1:4]) # [2, 3, 4]
print(my_list[1:]) # [2, 3, 4, 5]
print(my_list[:-1]) # [1, 2, 3, 4]

#reverse the list
print(my_list[::-1]) # [5, 4, 3, 2, 1]

#modify the list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # [1, 2, 3, 4, 5, 6]

#add 7 and 8 to the end of the list
my_list.extend([7, 8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8]

#add 9, 10, and 11
my_list.extend([9, 10, 11])
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#remove the last item
my_list.pop()
print(my_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#remove the item at index 2
my_list.pop(2)
print(my_list) # [1, 2, 4, 5, 6, 7, 8, 9, 10]

#sort the list in ascending order
my_list.sort()
print(my_list)  # [1, 2, 4, 5, 6, 7, 8, 9, 10]

#reverse the list
my_list.reverse()
print(my_list) 

#.remove to remove a specifc value
my_list.remove(4)
print(my_list)

#remove the last item
my_list.remove(10)
print(my_list)

new_list = list(range(12, 120))
print(new_list)
my_list.append(new_list)
print(my_list)

# 121 to 222
new_list1 = list(range(121, 222))
print(new_list1)
my_list.extend(new_list1)
print(my_list)

#every third character
print(my_list[::3])

#every tenth character
print(my_list[::10])

#remove every third element
del my_list[ : : 3]
print(len(my_list))
print(my_list)


#list functions
# .append() - adds an item tpo the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns an item at a given index
#   (default is the last item)
# .remove() - removes the first occurence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list

# why is a list more useful than a variable?
# A list can hold multiple values,
# while a variable can only hold one variable at a time

cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
# access the first item
print(cakes[0]) # chocolate
# access the last item
print(cakes[-1]) # carrot
# want strawberry instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
# change second cake to lemon
cakes[1] = 'lemon'
print(cakes)
# add a new cake to the end
cakes.append('cherry')
print(cakes)
# remove last cake
cakes.pop()
print(cakes)
# insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes)


# Examples:
my_list = ['apple', 'banana', 'cherry']
#  print(my_list[0])         # apple
#  print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

my_list2 = ['pizza', 'chicken', 'tacos', 'burger', 'sandwich']

# Print the second and last item.
print(my_list2[1])
print(my_list2[4])

# Add a new item using .append().

my_list2.append('mac and cheese')
print(my_list2)

# Remove the first item using .pop(0).
my_list2.pop(0)
print(my_list2)
# Reverse your list using .reverse().
my_list2.reverse()
print(my_list2)
