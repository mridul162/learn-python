# set1 = frozenset([1, 2, 3, 4, 5])
# set2 = frozenset([4, 5, 6, 7, 8])
#
# print("Original sets:")
# print(set1)
# print(set2)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# print("Difference of set1 and set2 using difference():")
# print(set1.difference(set2))
# print("Difference of set2 and set1 using difference():")
# print(set2.difference(set1))
# print("Difference of set1 and set2 using - operator:")
# print(set1 - set2)
# print("Difference of set2 and set1 using - operator:")
# print(set2 - set1)
####################################
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

bin_set = zip(integer, binary)

binary_dict = {k:v for k,v in bin_set}
print(binary_dict)
#####################################
# integer = [1, -2, 3, -4, 5, 6, -7, 8]
#
# add_inv = [-i for i in integer]
# print(add_inv)
####################################
# integer = [1, -2, 3, -3, 5, 6, -5, 2]
#
# sq_set = {i*i for i in integer}
# print(sq_set)