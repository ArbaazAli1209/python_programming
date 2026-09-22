# (Expression for item in iterable if condition)

daily_sales = [100, 200, 300, 400, 500]

total_cups = sum(sale for sale in daily_sales if sale > 200)
print(total_cups)