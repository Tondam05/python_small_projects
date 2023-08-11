# a = [1, 2, 3, 4, 5, 6]
import random

a = ["munna", "millioner", "mustang", "manager"]
# a_new = [item for item in a if len(item) >= 5]
#
# print(a_new)
import random
new_dict = {item: random.randint(1, 6) for item in a}
print(new_dict)
