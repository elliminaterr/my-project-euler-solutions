def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n


def distinct_primes_factors(x):
    num1_list = []
    num2_list = []
    num3_list = []
    num4_list = []
    

    num1 = prime_factors(x)
    for i in num1:
        num1_list.append(int(i))
        
    num1_list = list(set(num1_list))

    num2 = prime_factors(x+1)
    for i in num2:
        num2_list.append(int(i))
    
    num2_list = list(set(num2_list))
        
    num3 = prime_factors(x+2)
    for i in num3:
        num3_list.append(int(i))
        
    num3_list = list(set(num3_list))

    num4 = prime_factors(x+3)
    for i in num4:
        num4_list.append(int(i))
        
    num4_list = list(set(num4_list))
        
    if (len(num1_list) > 3) and (len(num2_list) > 3) and (len(num3_list) > 3) and (len(num4_list) > 3):
        print(x)

for i in range(3624,200000):
    distinct_primes_factors(i)

