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

list_of_primes = sieve_of_eratosthenes(10000)
odd_list = list(range(3,10000,2))
composite_list = [x for x in odd_list if x not in list_of_primes]

        
def generate_goldbach_numbers(n):
    goldbach_numbers = []
    for x in range(1,n):
        for y in list_of_primes:
            goldbach_numbers.append((y+2*(x**2)))
    return goldbach_numbers
            
goldbach_list = generate_goldbach_numbers(100000)

for a in composite_list:
    if a not in goldbach_list:
        print(a)
        break
