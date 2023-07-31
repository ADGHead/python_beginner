#name = "ahmed"
#age = 18
#gpa = 4.6

#print("My name is " + name)
#print("My age is " + str(age))
#print(f"My age is {age}")

#print("My name is %s" %name)
#print("My age is %d"%age)
#print("My gpa is %.2f"%gpa)

#print("My name is {}".format(name))
#print("My age is {}".format(age))
#print("My gpa is {}".format(gpa))


#name = input("Please input a name:\n")


#print(f"My name is {name}")


#IF, ELIF and ELSE
#name = "ahmed"
#print(name[1:])
#print(len(name))

name = input("Please input a name: \n")

if len(name) > 10:
    print(f"{name} is greater than 10 ")
elif len(name) > 7:
    print(f"{name} is greater than 7")
elif len(name) >= 5:
    print(f"{name} is greater than 5")
elif len(name) > 3:
    print(f"{name} is greater than 3")
else:
    print(f"{name} is greater than 0")
