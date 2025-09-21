# profit or loss
actual_amount = float(input("enter your actual price: "))
selling_price = float(input("enter your selling price: "))

if selling_price > actual_amount:
    print("your profit is", selling_price - actual_amount)
else:
    print("your loss is", selling_price - actual_amount)
