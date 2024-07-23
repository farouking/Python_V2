def number_of_food_groups():
    return 5
print(number_of_food_groups())
# This will print 5

#2
def number_of_military_branches():
    return 5



#3
def number_of_books_on_hold():
    return 5
    return 10  # This line will never be executed
print(number_of_books_on_hold())
# This will print 5 (the second return is never reached)

#4
def number_of_fingers():
    return 5
    print(10)  # This line will never be executed
print(number_of_fingers())
# This will print 5 (print inside function is never reached)

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()  # This function does not return a value, so x will be None
print(x)
# This will print 5 and None

#6
def add(b, c):
    return b + c  # Should return the sum instead of printing it
print(add(1, 2) + add(2, 3))
# This will print 8

#7
def concatenate(b, c):
    return str(b) + str(c)
print(concatenate(2, 5))
# This will print 25

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7  # This line will never be executed
print(number_of_oceans_or_fingers_or_continents())
# This will print 100 and 10 (the third return is never reached)

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3  # This line will never be executed
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) + number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
# This will print 7, 14, 21 (the third return is never reached)

#10
def addition(b, c):
    return b + c
    return 10  # This line will never be executed
print(addition(3, 5))
# This will print 8 (the second return is never reached)

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# This will print 500, 500, 300, 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# This will print 500, 500, 300, 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b = foobar()
print(b)
# This will print 500, 500, 300, 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# This will print 1, 3, 2

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# This will print 1, 3, 5, 10
