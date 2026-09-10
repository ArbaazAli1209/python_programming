# value = 13
# rem = value % 5

# if rem:
#     print(f"{value} is not divisible by 5, remainder is {rem}")

value = 13
if (rem := value % 5):
    print(f"{value} is not divisible by 5, remainder is {rem}")


available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter the size: ")) in available_sizes:
    print(f"{requested_size} is available")
else:
    print(f"{requested_size} is not available")


flavors = ["masala", "ginger", "lemon", "mint"]

if (requested_flavor := input("Enter the flavor: ")) not in flavors:
    print(f"{requested_flavor} is not available")

print(f"You chose {requested_flavor} chai")