products = ['phone','tablet','laptop','watch']

# display the products
print(f'The available products are: {products}')

remove_item = input('Enter product name to remove: ')

products.remove(remove_item)

print(f'Available products are: {products}')

# add product
add_product = input('Enter product name to add to the list: ')
add_after = input('Enter product name to add after: ')
index = products.index(add_after)

products.insert(index+1, add_product)

print(f'The available products are: {products}')