numbers = ['1','2','3','4','5','6','7','8','9']

print(numbers)
new_numbers = list(map(int, numbers))
print(new_numbers)

prices = [100,432,1312,2321,5443]
new_prices = list(map(lambda x: x-x*5/100,prices))
print(new_prices)


names = ['john','rob','mike']
new_names = list(map(str.capitalize,names))
print(new_names)