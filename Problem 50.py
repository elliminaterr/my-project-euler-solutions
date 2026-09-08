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
sum_checker_list = []

# Limit as adding numbers larger than 500,000 will overflow

for i in primes_list:
    if i > 500000:
        limit = (primes_list.index(i))
        break

# Had to test starting points to see when the biggest sum would be, too inefficient when automating

sum_primes = 0
for k in primes_list[3:limit]:
    sum_primes += k
    if sum_primes % 2 == 1:
        sum_checker_list.append(sum_primes)

largest_sum_sequence = 0

for x in sum_checker_list:
    if x in primes_list:
        if x > largest_sum_sequence:
            largest_sum_sequence = x
            
print(largest_sum_sequence)
