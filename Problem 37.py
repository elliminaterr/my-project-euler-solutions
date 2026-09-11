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

primes_list = sieve_of_eratosthenes(1000000)
truncatable_primes_list = []

for i in primes_list[4:]:
    truncatable = True
    for j in range(1,len(str(i))):
        if not (int(str(i)[j:]) in primes_list and int(str(i)[:(-j)]) in primes_list):
            truncatable = False
            break
    if truncatable:
        truncatable_primes_list.append(i)
print(sum(truncatable_primes_list))
