def total_cart_cost(cart):
    total = 0
    for item in cart:
        total += item['price'] * item['quantity']
        
    return total

cart = [
    {'name': 'banana', 'price': 5, 'quantity': 6},
    {'name': 'orange', 'price': 6, 'quantity': 5},
    {'name': 'apple', 'price': 10, 'quantity': 3}
]

print(total_cart_cost(cart))