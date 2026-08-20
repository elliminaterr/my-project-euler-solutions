num = 600851475143
prime = 2
while prime ** 2 <= num:
    if num % prime:
        prime += 1
    else:
        num = num // prime
        
print(num)
