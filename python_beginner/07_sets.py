# 1. Sets remove duplicate values:
s = {2, 3, 4, 3, 2, 6}
print("\n1. Sets remove duplicate values:", s)

# 2. Sets can store different types of values:
info = {"Carla", 29, False, 5.9, 29}
print("\n2. A single set can store different types of values: ", info)
print(type(info))

# 3. Creating empty dictionaries and sets:
print("\n3. Creating empty dictionaries and sets:")
harry = {}
print(type(harry))

potter = set()
print(type(potter))

# 4. Iterating through a set:
print("\n4. Iterating through a set:")
for value in info:
    print(value)
###########################

# s1 = {1, 2, 5, 6}
# s2 = {2, 4, 5, 7}

# print(s1.union(s2))
# s1.update(s2)
# print(s1)

# s_int = s1.intersection(s2)
# print(s_int)
# s1.intersection_update(s2)
# print(s1)

# s_sd = s1.symmetric_difference(s2)
# print(s_sd)
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1.isdisjoint(s2))
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# s1.add(7)
# s1.add(4)
# print(s1)
# print(s1.issuperset(s2))
# print(s2.issubset(s1))

# s1.remove(9)
# print(s1)
# s1.discard(9)
# print(s1)

# s1.pop()
# s1.pop()
# s1.pop()
# print(s1)

# del s1
# print(s1)

# s1.clear()
# print(s1)

# print(1 in s1)

