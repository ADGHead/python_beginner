def max_num(num_1, num_2, num_3):
    if num_1 > num_2 and num_1 > num_3:
        print(str(num_1) + " is the biggest")
    
    elif num_2 > num_1 and num_2 > num_3:
        print(str(num_2) + " is the biggest")

    else:
        print(str(num_3) + " is the biggest")

num_1 = int(input("Please input a number \n"))
num_2 = int(input("Please input a second number \n"))
num_3 = int(input("Please input a third number \n"))

max_num(num_1, num_2, num_3)