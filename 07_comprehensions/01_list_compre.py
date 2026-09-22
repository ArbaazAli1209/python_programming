menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Chai"
]

# [Expression for item in iterable if condition]
# iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]
iced_tea = [my_tea for my_tea in menu if len(my_tea) < 12]

print(iced_tea)