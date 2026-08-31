names_list = []
with open("0022_names.txt") as f:
    names_list = list(eval(f.read()))
names_list.sort()
final_sum = 0

for x in range(1,len(names_list)+1):
    name_sum = 0
    for y in names_list[x-1]:
        name_sum += (ord(y)-64)
    final_sum += (x * name_sum)

print(final_sum)
