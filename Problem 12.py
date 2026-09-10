import math

def generate_triangle_numbers(n):
    triangle_number = 0
    triangle_list = []
    aggregator = 1
    
    while triangle_number < n:
        triangle_number += aggregator
        triangle_list.append(triangle_number)
        aggregator += 1
        
    return triangle_list

def get_divisors(n):
    divisors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
                
    return divisors

triangle_numbers = generate_triangle_numbers(100000000)
for i in triangle_numbers:
    if len(get_divisors(i)) > 500:
        print(i)
