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

primes_list = sieve_of_eratosthenes(10000000)

def pandigital_checker():
    big_pandigital = 0
    fail_condition = True
    for i in primes_list:
        if len(str(i)) < 6:
            pass
        else:
            checker = [int(y) for y in str(i)]
            for x in range(len(str(i))):
                if (list(range(1,len(str(i))+1))[x] not in checker):
                    fail_condition = True
                    break
                else:
                    fail_condition = False
        if fail_condition:
            pass
        else:
            big_pandigital = i
    return big_pandigital

print(pandigital_checker())
