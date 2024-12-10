a = {1,2,3,4,5}
print(a)
a.add(6)
print(a)
a.discard(3)
last = a.pop()
print(a)
print(last)
a.clear()
print(a)
# if you use remove instead of discard but
# it give you an error if the element is not found in set
# so if you sure the element is present the you can use remove otherwise
# you have to use discard method
# pop method pop the element randomly
# clear() method clear the set or empty the set