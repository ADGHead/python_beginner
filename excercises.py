#def multiplication_table(x):
    #table = 0
    #values = 1
    #while table < 12:
        #multiplication = values*x
        #print(multiplication)
        #values+=1
        #table+=1
        

#multiplication_table(4)

#def count_numbers(x):
    #string_numbers = str(x)
    #count = 0
    #while count < len(string_numbers):
        #for i in string_numbers:
            #count+=1
        #print(count)

#count_numbers(1000000)

#for i in range(-10,-1):
    #print(i)

#def is_prime(x):
    #if x < 2:
        #return False
    #elif x ==2:
        #return True
    #for n in range(2, x):
        #if x%n == 0:
            #return False
    #return True

#def generator(a,b):
    #for i in range(a,b):
        #if is_prime(i):
            #yield i
            

#num_1 = int(input("Please input a number: "))
#num_2 = int(input("Please input another number: "))

#print(list(generator(num_1, num_2)))

def fibonnaci(x):
    count = 0
    first_num = 0
    second_num = 1
    result = ""
    final = ""
    while count < x:
        num = first_num + second_num
        next_num = num + second_num
        first_num = num
        second_num = next_num
        count += 1
        result = str(num)  + " " + str(next_num)
        final = final + " " + result
        final_result =final.split()
        final_result_2 = " ".join(final_result)
    print(final_result_2)

fibonnaci(5)







