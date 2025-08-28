"""
📝 List Operations Assignment
Author: Oluwalayomi Jesuloluwa

This program demonstrates basic list operations in Python:
1. Create an empty list.
2. Append elements.
3. Insert an element at a specific position.
4. Extend the list with another list.
5. Remove the last element.
6. Sort the list in ascending order.
7. Find and print the index of a specific value.
"""

# 1. Create an empty list
my_list = []

# 2. Append elements: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending 10, 20, 30, 40:", my_list)

# 3. Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at second position:", my_list)

# 4. Extend with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# 5. Remove the last element
my_list.pop()
print("After removing the last element:", my_list)

# 6. Sort the list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# 7. Find and print the index of the value 30
index_30 = my_list.index(30)
print("The index of 30 is:", index_30)
