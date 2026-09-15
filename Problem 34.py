def factorial(n):
    if n == 0:
        return 1
    output = n
    while n > 1:
        output*= (n-1)
        n -= 1
    return output

final_sum = 0
for i in range(3,100000):
    if i == sum([factorial(int(x)) for x in str(i)]):
        final_sum += i
print(final_sum)
