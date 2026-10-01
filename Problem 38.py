def check_unique_digits(i):
    i = str(i)
    seen_list = []
    for x in i:
        if x in seen_list or x == "0":
            return False
        else:
            seen_list.append(x)
    return True
        
pandigital_num = ""
final_pandigital = 0
for i in range(1,100000000):
    is_pandigital = True
    counter = 1
    while is_pandigital and (len(pandigital_num) < 8):
        if check_unique_digits(i * counter):
            pandigital_num += str(i * counter)
            counter += 1
        else:
            is_pandigital = False
    if pandigital_num != "": 
        if int(pandigital_num) > final_pandigital and check_unique_digits(pandigital_num) and len(pandigital_num) == 9:
            final_pandigital = int(pandigital_num)
    pandigital_num = ""
print(final_pandigital)
