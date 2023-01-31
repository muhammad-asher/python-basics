customer = {
    "name": "Asher",
    "age": 30,
    'is_verified': True
}
print(customer.get('name'))
print(customer.get('BirthDate','August 03 2000'))
customer['name']="Abdullah"
print(customer.get('name'))

