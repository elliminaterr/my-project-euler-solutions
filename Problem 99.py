import math
base_exponent_pairs = []
with open("0099_base_exp.txt") as f:
    base_exponent_pairs = f.read().split("\n")
f.close()
x = []
base_exponent_list = []
max_number = 0
for a in base_exponent_pairs:
    x = a.split(",")
    x = [int(y) for y in x]
    base_exponent_list.append(x)

for i in base_exponent_list:
    if (i[1] * math.log(i[0],10)) > max_number:
        max_number = (i[1] * math.log(i[0],10))
        max_index = base_exponent_list.index(i)
print(max_index)
