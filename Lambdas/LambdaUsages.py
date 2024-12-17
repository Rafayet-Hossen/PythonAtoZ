numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(x):
    return x ** 2
#map function return an object
lists = list(map(square, numbers))
list_modified = list(map(square, lists))
print(lists)
print(list_modified)