distinct_powers_list = []
for a in range(2,101):
    for b in range(2,101):
        distinct_powers_list.append(pow(a,b))
        
distinct_powers_list = list(set(distinct_powers_list))
print(len(distinct_powers_list))
