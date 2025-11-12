# An example of functions in Python
tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

# Without using functions, repeating same statements
total = 0
for item in tom_exp_list:
    total= total+item
print("Tom's total expenses: ", total)

total = 0
for item in joe_exp_list:
    total= total+item
print("Joe's total expenses: ", total)

# Using functions to avoid repetition
def calculate_total(exp):
    total = 0
    for item in exp:
        total = total+item
    return total

toms_total= calculate_total(tom_exp_list)
joes_total= calculate_total(joe_exp_list)

print("Tom's total expenses: ", toms_total)
print("Joe's total expenses: ", joes_total)

# Function with default argument
# total=0           # global variable
def sum(a,b=0):
    """
    This function takes two arguments which are integer numbers,
    and it will return sum of them as an output.
    :param a:
    :param b:
    :return: 
    """
    print("a: ", a)
    print("b: ", b)
    total= a+b      # local variable
    print("Total Inside: ", total) #
    return total  

n = sum(5)
print("Total Outside: ", n)
print("Total Outside: ", total)

# Function with multiple return values
def arithmetic_operations(x, y):
    add = x + y
    sub = x - y
    mul = x * y
    div = x / y
    return add, sub, mul, div

a, s, m, d = arithmetic_operations(10, 5)
print("Addition: ", a)
print("Subtraction: ", s)
print("Multiplication: ", m)
print("Division: ", d)
result = arithmetic_operations(20, 4)
print("Results as a tuple: ", result)

# Function with variable number of arguments
def multiply(*args):
    result = 1
    for num in args:
        result = result * num
    return result
print("Multiplication of 2, 3: ", multiply(2, 3))
print("Multiplication of 2, 3, 4, 5: ", multiply(2, 3, 4, 5))
print("Multiplication of 1, 2, 3, 4, 5, 6: ", multiply(1, 2, 3, 4, 5, 6))

# Function with keyword arguments
def person_info(name, age, city):
    print("Name: ", name)
    print("Age: ", age)
    print("City: ", city)
person_info(age=30, city="New York", name="Alice")
person_info("Bob", city="Los Angeles", age=25)
person_info("Charlie", 28, "Chicago")