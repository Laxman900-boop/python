products = [
    {"name": "Watch", "price":  12},
    {"name": "Laptop", "price": 34},
    {"name": "I-phone", "price": 50},
    {"name": "T.V", "price": 12},
]

Company = [
    {"name": "National post", "fees": 250},
    {"name": "White house ", "fees": 100},
    {"name": "LK express", "fees": 300},
    {"name": "DH express", "fees": 100},
    ]

print("List of products:")
for product in products:
    print(f"For{product["name"]} press {index}")


while True:
    user_product_index = input("please enter the product number:\n")

    try:

        if user_product_index >= 0 and user_product_index < len(products):
             break
        else:
             print("this product does not exit")

    except ValueError:
        print("please enter only number")

user_product = product{user_product_index}