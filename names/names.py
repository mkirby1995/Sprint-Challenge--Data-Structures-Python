import time
from bst import BinarySearchTree


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

"""
duplicates = []
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
"""

# Initialize tree with first value of names_1
tree = BinarySearchTree(names_1[0])

# for each name in names_1
for name in names_1[1:]:
    # Insert name into tree
    tree.insert(name)

# Initialize a dupes list
duplicates = []

# for each name in names_2
for name in names_2:
    # check if tree contains name
    # If it does
    if tree.contains(name):
        # Add it to dupes list
        duplicates.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
