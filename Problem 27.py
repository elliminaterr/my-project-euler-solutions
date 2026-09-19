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

primes_list = sieve_of_eratosthenes(10000)

possible = True
solution_works = True
final_list = []

while possible:
    n = 0
    for a in range(-1000,1001):
        for b in range(-1000,1001):
            solution_works = True
            while solution_works:
                if ((n**2) + (a * n) + b) in primes_list:
                    n += 1
                else:
                    final_list.append((n,a*b))
                    solution_works = False
                    n = 0
    possible = False
print(max(final_list)[1])
