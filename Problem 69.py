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

max_etf_divided = 0
max_num = 0
for i in range(1,1000000):
    etf_divided = i / etf(i)
    if etf_divided > max_etf_divided:
        max_etf_divided = etf_divided
        max_num = i
print(max_num)
