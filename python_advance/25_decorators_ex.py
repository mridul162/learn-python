def is_non_negative_int(func):
    def helper(x):
        if type(x) == int and x>=0:
            return func(x)
        else:
            raise Exception("Argument is not a non-negative integer!")

    return helper

@is_non_negative_int
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-5))

