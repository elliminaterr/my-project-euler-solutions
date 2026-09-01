final_sum = 0
for i in range(2,1000000):
    num_list = [int(x) for x in str(i)]
    sum_powers = 0
    for y in num_list:
        sum_powers += pow(y,5)
    if sum_powers == i:
        final_sum += i
print(final_sum)
