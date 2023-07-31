
def cube_number(num):
    cube = num*num*num
    return cube

print(cube_number(8))

def calc(side):
    p = 4 * side
    a = side*side
    return p, a

p, a = calc(4)

print("The perimeter of the square is : " + str(p) + " and The area of the square is : " + str(a))