cart = []

while True:
    user_input = input("Enter item price (or 'q' to quit): ")

    if user_input.lower() == 'q':
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Negative price not allowed")

        cart.append(price)
        print("Price added successfully.")

    except ValueError as e:
        print("Error:", e)

print("\nTotal items:", len(cart))
print("Total bill:", sum(cart))