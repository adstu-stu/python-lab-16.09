def generate_bill(*args, **kwargs):
    if not args or not kwargs:
        print("Item prices and quantities are required.")
        return

    if len(args) != len(kwargs):
        print("Mismatch: number of prices must match number of items.")
        return

    items = list(kwargs.items())  # [(name, quantity), ...] in order given
    prices = list(args)

    total_bill = 0
    total_quantity = 0

    print("Item Details:")
    for (name, qty), price in zip(items, prices):
        item_total = price * qty
        total_bill += item_total
        total_quantity += qty
        print(f"  {name}: Price=₹{price}, Qty={qty}, Subtotal=₹{item_total}")

    average_price = sum(prices) / len(prices)

    discount = 0
    if total_bill > 5000:
        discount = total_bill * 0.10

    final_amount = total_bill - discount

    print("\nTotal Bill: ₹{:.2f}".format(total_bill))
    print("Total Quantity:", total_quantity)
    print("Average Price: ₹{:.2f}".format(average_price))
    print("Discount Applied: ₹{:.2f}".format(discount))
    print("Final Payable Amount: ₹{:.2f}".format(final_amount))


# Example
generate_bill(500, 1200, 300, Pen=10, Notebook=4, Eraser=20)