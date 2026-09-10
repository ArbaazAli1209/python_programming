staff = [("Amit", 16), ("Zara", 15), ("Raj", 17)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
# Fall back else block will execute if the loop is not broken
else:
    print("No one is eligible to manage the staff")    