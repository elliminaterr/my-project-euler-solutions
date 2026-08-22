def factorial_sum(n):
    counter = 1
    for i in range(1,n):
        counter *= i
    digit_sum = sum([int(x) for x in str(counter)])
    return digit_sum

print(factorial_sum(100))
