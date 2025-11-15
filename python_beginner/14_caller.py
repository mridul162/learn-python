# Caller script to demonstrate importing a module
import area
print("I am in caller.py")
area = area.calculate_area(5,6)
print(area)