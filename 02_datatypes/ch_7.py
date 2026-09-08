# Tuples
masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 1,2
print(f" Ratio of G: {ginger_ratio} and C: {cardamom_ratio}")
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f" Ratio of G: {ginger_ratio} and C: {cardamom_ratio}")

# Membership

print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")