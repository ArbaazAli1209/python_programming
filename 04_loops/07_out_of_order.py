flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of stock":
        continue
    elif flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"Available item: {flavour}")

print("Outside of loop")    