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

primes_list = sieve_of_eratosthenes(1000)

# Unique repeating sections will come from prime denominators

primes_list.remove(2)
primes_list.remove(5)

# These two numbers cause infinite loops so are removed immediately

counter = 1
biggest_counter = 0
biggest_repeat = 0
biggest_decimal = 0

for i in primes_list:
    counter = 1
    while ((pow(10,counter)-1) % i) != 0:
        counter += 1
    if counter > biggest_counter:
        biggest_counter = counter
        biggest_repeat = counter / i
        biggest_decimal = i
        
# Division by 2 or 5 or 10 causes the repeated section to increase by 1 so we add 1

print(biggest_counter+1)
        
