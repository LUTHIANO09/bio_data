def add_greetings(func):
    def inner(name ):
        return "Good Morning, " + func(name).upper()
    return inner

@add_greetings
def greetings(name):
    return name

print(greetings("ibrahim"))

# NO 1
def add(y):
    return 10+y
print(add(5))

# NO 2
def sub(x):
    return x-5
print(sub(20))

# NO 3
def multiply(x):
    return x*3
print(multiply(4))

# NO 4
def divide(x):
    return x/2
print(divide(10))

# NO 5
def square(x):
    return x**2
print(square(6))

# NO 5
def cube(x):
    return x**3
print(cube(3))

# NO 6
def double(x):
    return x*2
print(double(7))

# NO 7
def returns_remainder(x):
    return x%4
print(returns_remainder(17))

# NO 8
def by_100(x):
    return x+100
print(by_100(50))

# NO 9
def negative(x):
    return 0-x
print(negative(9))

# NO 10
def takes_two(x,y):
    return x+y
print(takes_two(3,7))

# NO 12
def sub_two(x,y):
    return y-x
print(sub_two(15,4))

# NO 13
def two_mul(x,y):
    return x*y
print(two_mul(6,5))

# NO 14
def two_div(x,y):
    return x/y
print(two_div(20,4))

# NO 15

def retuns_larger(x,y):
    if y > x:
        return y
    elif y < x:
        return x
    else:
        return "error"
print(retuns_larger(8,12))

#NO 16
def retuns_smaller(x,y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return "error"
print(retuns_smaller(8,12))

#NO 17
def return_avg(x,y):
    avg=x+y
    return avg/2
print(return_avg(10,20))

#NO 18
def raises(x,y):
    return x**y
print(raises(2,8))

#NO19
def returns_sum(x,y):
    s1= x**2
    s2= y**2
    return s1+s2
print(returns_sum(3,4))

#NO 20
def true(x,y):
    if x > y:
        return True
    else:
        return False
print(true(10,5))

# NO 21
def three(x,y,z):
    return x+y+z
print(three(5,6,2))

#NO 22
def three_m(x,y,z):
    return x*y*z
print(three_m(2,3,4))

#NO 23
def three_returns(x,y,z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    elif z > x and z > y:
        return z
print(three_returns(10,25,18))

#NO 24
def ret_avg(x,y,z):
    avg=x+y+z
    return avg/3
print(ret_avg(10,20,30))

#NO 25

def equals(x,y,z):
    if x == y and z == y: return True
    elif x == z:
        return False
    else:
        return False
print(equals(5,5,5))

#NO 26
def total_sum(x,y,z):
    sm=x+y+z
    return sm - 2
print(total_sum(4,7,2))

#NO 27

def ret_true(x,y,z):
    first2= x+y
    if first2 > z:
        return True
    else:
        return False
print(ret_true(3,4,5))

#NO 28
def product_of_2(x,y,z):
    f2=x*y
    return f2/z
print(product_of_2(10,6,3))

#NO 29