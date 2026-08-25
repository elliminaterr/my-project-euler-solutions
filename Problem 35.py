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
circular_primes = []

for x in primes_list:
    checker = [i for i in str(x)]
    fail_condition = False
    for y in range(len(checker)-1):
        checker.append(checker[0])
        checker.remove(checker[0])
        if int("".join(checker)) in primes_list:
            pass
        else:
            fail_condition = True
            break
    if fail_condition:
        pass
    else:
        circular_primes.append(checker)

print(len(circular_primes))
