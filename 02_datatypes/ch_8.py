ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients are: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients are: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last added ingredient: {last_added}")
print(f"Chai ingredients are: {chai_ingredients}")
chai_ingredients.reverse()
print(f"Chai (reversed): {chai_ingredients}")
chai_ingredients.sort()
print(f"Chai (sorted): {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")

# Operator Overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")