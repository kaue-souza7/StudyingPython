product = {
    'name': 'Laptop',
    'brand': 'Dell',
    'price': 1500.00,
    'stock': 50,
    'available': True
}

for attribute in product:
    print(attribute, product[attribute])








def delete_attribute(attribute):
    del product[attribute]
    print('Item deletado!')
    
# delete_attribute('stock')




    
def add_attribute(attribute_name, attribute_value):
    product[attribute_name] = attribute_value
    print('Product added successfully')

# add_attribute('Color', 'Gray')





def attribute_modify(attribute_old, attribute_new, attribute_value):
    del product[attribute_old]
    product[attribute_new] = attribute_value
    print('Product modified sucessfully')

attribute_modify('stock', 'Color', 'Gray')






for attribute in product:
    print(attribute, product[attribute])

    





