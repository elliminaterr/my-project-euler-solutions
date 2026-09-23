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
primes_list = [x for x in primes_list if len(str(x)) > 3]
final_number = 0
final_list = []
for i in range(len(primes_list)):
    num_list1 = sorted([int(x) for x in str(primes_list[i])])
    for j in range(len(primes_list)):
        num_list2 = sorted([int(x) for x in str(primes_list[j])])
        if (i != j) and (num_list1 == num_list2) and j > i:
            final_number = primes_list[j] + (primes_list[j]-primes_list[i])
            num_list3 = sorted([int(x) for x in str(final_number)])
        if final_number in primes_list and num_list1 == num_list3:
            final_list.append(str(primes_list[i])+str(primes_list[j])+str(final_number))
            
print(final_list)
