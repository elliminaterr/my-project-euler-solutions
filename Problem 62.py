cubes_list = []
for i in range(3,10000):
    cubes_list.append(i**3)

counter = 0
for a in cubes_list:
    counter = 0
    for b in cubes_list:
        if len(str(a)) == len(str(b)):
            a_list = sorted([x for x in str(a)])
            b_list = sorted([y for y in str(b)])
            if a_list == b_list:
                counter += 1
    if counter == 5:
        print(a)
        break
