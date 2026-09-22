# {Expression for item in iterable if condition}

favourite_chais = [
    "Masala chai", "Green tea", "Masala chai", 
    "Lemon tea", "Green tea", "Elaichi chai"
]

unique_chai = {chai for chai in favourite_chais if len(chai) > 8}
print(unique_chai)

recipes = {
    "Masala Chai": ["water", "milk", "sugar", "tea leaves", "spices"],
    "Iced Lemon Tea": ["water", "lemon", "sugar", "ice"],
    "Green Tea": ["water", "green tea leaves"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)