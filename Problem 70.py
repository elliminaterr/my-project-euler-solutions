def etf(num):

    result = num
    prime = 2
    while (prime * prime) <= num:

        if num % prime == 0:
            while num % prime == 0:
                num //= prime

            result -= result // prime
        prime += 1
    if num > 1:
        result -= result // num

    return result


totient_ratio_list = []
for i in range(2,10000000):
    if sorted([x for x in str(i)]) == sorted(y for y in str(etf(i))):
        totient_ratio_list.append((i/etf(i),i))
print(min(totient_ratio_list))
