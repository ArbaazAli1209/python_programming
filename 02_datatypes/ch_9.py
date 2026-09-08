# Dictionary
# Type 1
chai_order = dict(type="Masala Chai", size="Medium", sugar=3)
print(f"Chai order: {chai_order}")

# Type 2
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Chai recipe: {chai_recipe['base']}")
print(f"Chai recipe: {chai_recipe}")
# Deletion of a key-value pair from a dictionary
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")

# Type 3
chai_order = {"type": "Masala Chai", "size": "Large", "sugar": 2}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")

extra_spices = {
    "cardamom": "crushed",
    "ginger": "sliced"
}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("note", "No note")
print(f"Customer note: {customer_note}")