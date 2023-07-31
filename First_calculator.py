

arithmetic = input("Please input the arithmetic that you would like to perform \n")

if arithmetic == "addition":
    def addition(x,y):
        add = x + y
        print("The sum of these two numbers is: ",  add)
        return add
    num_1 = int(input("please input your first number \n"))
    num_2 = int(input("please input your second number \n"))
    addition(num_1,num_2)

if arithmetic == "subtraction":
    def subtraction(x,y):
        sub = x-y
        print("The subtraction of these two numbers is:", sub)
        return sub
    num_1 = int(input("please input your first number \n"))
    num_2 = int(input("please input your second number \n"))
    subtraction(num_1,num_2)

if arithmetic == "multiplication":
    def multiplication(x,y):
        mult = x*y
        print("The multiplication of these 2 numbers is:", mult)
        return mult
    num_1 = int(input("please input your first number \n"))
    num_2 = int(input("please input your second number \n"))
    multiplication(num_1,num_2)

if arithmetic == "division":
    def division(x,y):
        div = x/y
        print("The division of these 2 numbers is:", div)
        return div
    num_1 = int(input("please input your first number \n"))
    if num_1 == 0:
        num_1 = int(input("please input another number \n"))
    num_2 = int(input("please input your second number \n"))
    if num_2 == 0:
        num_2 = int(input("please input another number \n"))
    division(num_1,num_2)
