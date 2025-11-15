# Exception Handling in Python
# This script demonstrates how to handle exceptions using try-except blocks.

x = input("Enter a num1: ")
y = input("Enter num2: ")

try:                                        # Try block to catch exceptions
    # z= int(x)/ int(y)
    z= x/ int(y)
# except Exception as e:                    # Catch all exceptions
#     print('Exception Occurred: ', e)      # Print the exception message

except ZeroDivisionError as e:
    print('Division by Zero Occurred!')
    z= None
except Exception as e:
    print('Exception type: ', type(e).__name__)
    z= None

print("Division is: ", z)