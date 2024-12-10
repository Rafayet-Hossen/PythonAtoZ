s1 = set([1,4,6,7,4,0])
s2 = set([1,7,8,4])
print(s1)
print(5 in s1)
print(4 in s1)
print(s1.union(s2)) # s1 | s2 is similar to union
print(s1.intersection(s2)) # s1 & s2 similar to intersection
print(s1.difference(s2)) # s1 - s2 similar to difference
print(s1.symmetric_difference(s2)) # s1 ^ s2 similar to symmetric difference