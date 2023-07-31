#Pile of stones Excercise
def no_stones(x):
    list_giving = []
    count = 0
    while len(list_giving) < x:
        specification = count + x
        list_giving.append(specification)
        count += 2
    print(list_giving)

integers = int(input("Please input a number:\n"))
no_stones(integers)