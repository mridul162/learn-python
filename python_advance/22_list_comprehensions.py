numbers = [1,2,3,4,5,6,7,8]
even = [i for i in numbers if i%2==0]
print(even)

s = set([1,2,3,4,2,3])
print(s)
even = {i for i in s if i%2==0}
print(even)

cities=["dhaka", "mumbai", "new work", "paris"]
countries=["bangladesh", "india", "usa", "france"]
z = zip(cities, countries)
for a in z:
    print(a)

d= {city:country for city, country in zip(cities,countries)}
print(d)