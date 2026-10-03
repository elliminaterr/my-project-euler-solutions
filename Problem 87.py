import math

def sieve_of_eratosthenes(n):
    prime_list = []
    prime = [True for _ in range(n + 1)]
    prime[0], prime[1] = False, False

    for p in range(2, int(math.sqrt(n)) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    for i in range(2, n + 1):
        if prime[i]:
            prime_list.append(i)
    return prime_list

def get_limits(num_list):  
    for i in num_list:
        if (i**2) > 50000000:
            SQUARE_LIMIT = num_list.index(i)
            break
    for i in num_list:
        if (i**3) > 50000000:
            CUBE_LIMIT = num_list.index(i)
            break
    for i in num_list:
        if (i**4) > 50000000:
            FOURTH_POWER_LIMIT = num_list.index(i)
            break
    return SQUARE_LIMIT, CUBE_LIMIT, FOURTH_POWER_LIMIT
    
primes_list = sieve_of_eratosthenes(50000000)
x,y,z = get_limits(primes_list)

final_list = []
for i in range(x):
    for j in range(y):
        for k in range(z):
            new_num = primes_list[i]**2 + primes_list[j]**3 + primes_list[k]**4
            if new_num < 50000000:
                final_list.append(new_num)
print(len(list(set(final_list))))
