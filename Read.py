#employee_file = open(r"C:\Users\USER\Desktop\AHMED\Python_Beginner\For.py", "r")
#print(employee_file.read())

# The readable function is used to find whether the file is readable
#print(employee_file.readable())

# The readline is used to read an individual line in the selected file
# You can also call the specific lines using the index of the lines
# You can also loop it
#print(employee_file.readline())

# The readlines function is used to store all the lines in the file in a list
#print(employee_file.readlines())

#employee_file.close()
#You have to always close a file after you open it

#open("for.py", "w")
#open("for.py", "a")
#open("for.py", "r+")

# The open function is used to open a file from your computer
# There are two segments needed to be added to open the file
# That is the name of the file and how you want the file to be opened
# r is used to open the file in read mode
# w is used to open the file in write mode
# a is used to append information to the end of the selected file
# r+ is used to open the file in read and write mode

with open(r"C:\Users\USER\Desktop\AHMED\Python_Beginner\For.py", "a") as file:
    file.write("Ahmed Babatunde")
    file.close()