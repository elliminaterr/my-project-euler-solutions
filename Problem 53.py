def factorial(n):
    counter = n
    if n == 0:
        return 1
    while counter > 2:
        n *= (counter-1)
        counter -= 1
    return n
        
def combinatoric_function(n,r):
    if r <= n:
        return (factorial(n) / (factorial(r) * factorial(n - r)))

counter = 0
for i in range(23,101):
    for j in range(1,i):
        if combinatoric_function(i,j) > 1000000:
            counter += 1


print(counter)
