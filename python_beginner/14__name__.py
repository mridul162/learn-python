# Demonstration of __name__ variable:
import modules.area as a

def calculate_area(base,height): 
    print("__name__: ", __name__)            # Print the __name__ variable
    return 1/2 * (base*height)

if __name__ == "__main__":                   # This block will execute only if this script is run directly
    print("I am in __name__.py")
    area1 = calculate_area(10, 20) 
    print("Area from __name__.py: ", area1)
    
    area2 = a.calculate_area(10, 20)         # Importing and using function from another module
    print("Area from imported module: ", area2)
