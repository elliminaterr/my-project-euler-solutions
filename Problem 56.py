digit_sum_list = []
for a in range(1,100):
    for b in range(1,100):
        digit_sum_list.append(sum([int(x) for x in str(pow(a,b))]))
print(max(digit_sum_list))
