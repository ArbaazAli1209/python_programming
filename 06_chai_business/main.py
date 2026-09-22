# import recipes.flavors

# print(recipes.flavors.elaichi_chai())

from recipes.flavors import elaichi_chai, ginger_chai, masala_chai
from utils.discounts import chai_discount

print(ginger_chai())
print(chai_discount(100, 10))