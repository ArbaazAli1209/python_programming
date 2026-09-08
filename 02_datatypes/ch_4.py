is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling    # upcasting boolean to integer
print(f"Total actions: {total_actions}")
print(f"Boiling status: {is_boiling}")

milk_present = 0
print(f"Milk present? {bool(milk_present)}")

water_hot = True
tea_added = True
can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")