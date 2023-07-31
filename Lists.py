integers = [4, 5, 6, 7, 8, 9]
words = ["Intellectual", "Cowardice", "Proponent", "Causal"]
#The copy function is used to copy all the elements in a particular list to a new list
words_2 = words.copy()

# The extend function is used to join 2 lists together
words.extend(integers)

# The append function is used to add a new element to the end of a list
words.append("Luxury Cracking")

#The insert function inserts a new element into a list using two parameters the postion(index) and the name of the element
words.insert(1, "Nuclear Fission")

#The remove function is used to remove any element contained  in the list
words.remove("Proponent")

#The pop function is used to pop an element of the list
words.pop(6)

#The sort function is used to sort elements in a list
#words.sort()

#The reverse function is used to reverse the arrangements of elements in a list
words.reverse()

#The index function is used to find the index position of the element contained in the list
print(words.index("Luxury Cracking"))

#The count function is used to find the amount of times an element appears in a list
print(words.count("Nuclear Fission"))

#The clear function is used to reset the list
#words.clear()

#The sorted function sorts the list
#my_sorted_list = sorted(words)

print(integers)
print(words)
print(words_2[0])