def find_divisors_generator(n):
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            yield i
            if i != n // i:
                yield n // i     

abundant_list = []
possible_sums = []
final_list = []

for i in range(1,21823):   
    divisor_sum = (sum(list(find_divisors_generator(i))) - i)
    if divisor_sum > i:
        abundant_list.append(i)

for j in range(len(abundant_list)):
    for k in range(len(abundant_list)):
        possible_sums.append(abundant_list[j]+abundant_list[k])
possible_sums = list(set(possible_sums))

for a in range(1,21824):
    if a not in possible_sums:
        final_list.append(a)
print(sum(final_list))
    
