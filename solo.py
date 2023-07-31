#FUNCTONAL PROGRAMMING
#def apply_twice(func, arg):
#   return func(func(arg))

#def add_five(x):
#    return x + 5

#print(apply_twice(add_five, 10))

#def test(func, arg):
#    return func(func(arg))

#def mult(x):
#    return x*x

#print(test(mult, 2))

#LAMBDA
#print((lambda x: x**2 + 5*x + 4)(-4))

#price = int(input())
#perc = float(input())

#res = (lambda x,y : x*(y/100))(price,perc)

#print(res)

#MAP AND FILTERS
#def add_five(x):
#    return x+5

#nums = [11, 22, 33, 44, 55]
#result = list(map(add_five, nums))
#print(result)

#nums = [11, 22, 33, 44, 55]

#result = list(map(lambda x: x+5, nums))
#print(result)

#nums = [11, 22, 33, 44, 55]
#res = list(filter(lambda x: x%2==0, nums))
#print(res)

#GENERATORS
#def countdown():
    #i = 5
    #while i>0:
        #yield i
        #i -= 1

#for i in countdown():
    #print(i)

#def numbers(x):
    #for i in range(x):
        #if i % 2 == 0:
            #yield i

#print(list(numbers(11)))

#def isPrime(x):
    #if x<2:
        #return False
    #elif x ==2:
        #return True
    #for n in range(2, x):
        #if x % n ==0:
            #return False
    #return True

#def primeGenerator(a,b):
    #for i in range(a, b):
        #if isPrime(i) == True:
            #yield i

#f = int(input())
#t = int(input())

#print(list(primeGenerator(f,t)))

#Decorators
#def decor(func):
    #def wrap():
        #print("============")
        #func()
        #print("============")
    #return wrap

#def print_text():
    #print("Hello World!")

#decorated = decor(print_text)
#decorated()

#def decor(func):
    #def wrap(num):
        #print("***")
        #func(num)
        #print("***")
        #print("END OF PAGE")
    #return wrap

#@decor
#def invoice(num):
    #print("INVOICE #" + num)

#invoice(input());

#Recursion
#def factorial(x):
    #if x==1:
        #return 1
    #else:
        #return x * factorial(x-1)
    
#print(factorial(5))

#def is_even(x):
    #if x == 0:
        #return True
    #else:
        #return is_odd(x-1)
    
#def is_odd(x):
    #return not is_even(x)

#print(is_odd(17))
#print(is_even(23))

#def convert(num):
    #if num == 0:
        #return 0
    #return (num % 2 + 10 * convert(num//2))

#integer = int(input("Please enter a number : "))

#print(convert(integer))