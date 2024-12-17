def odd_generator(x):
    for i in range(x+1):
        if i%2 != 0:
            yield i

odd_list = list(odd_generator(10))
print(odd_list)