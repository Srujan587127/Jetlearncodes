#set operations
#union - everything/together
#intersection - similarites between the things
#diferences - Elements that exist in A subset, but not B subset
#symetric differences - union minus intersections

set_a = {1,2,3,4,5}
set_b = {4,5,6,7,8}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))
print(set_a.symmetric_difference(set_b))



apple = [1,2,3,4,5,6,7,8,9,9,8,7,6]
sample_set = set(apple)
print(sample_set)

if 10 in sample_set:
    print("no")
else:
    print("no")

my_set = set([])
my_set.add(23)
my_set.add(22)
my_set.add(43)
print(my_set)
my_set.discard(100)
print(my_set)
