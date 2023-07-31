#def add_it_up(x):
    #nums = 1
    #for i in range(x):
        #nums+=i
        #result = nums + i
    #return result

#integer = int(input("Please enter a number: \n"))
#print(add_it_up(integer))

def add_it_up(x):
    add =[]
    for i in range(x):
        add.append(i)
    from functools import reduce
    adding = reduce(lambda x,y : x+y,add)
    print(adding)

add_it_up(11)
