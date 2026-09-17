def proper_divisor_sum(n):
    return_list = [0]
    
    for i in range(1,n):
        if n % i == 0:
            if i == return_list[-1]:
                break
            elif i == 1:
                return_list.append(i)
            else:
                return_list.append(i)
                return_list.append(n // i)

    return sum(list(set(return_list)))

def amicable_numbers(n):
    return_sum = 0
    for i in range(1,n):
        d = proper_divisor_sum(i)
        if (i == proper_divisor_sum(d)) and (d != i):
            return_sum += i
            return_sum += d
    return_sum /= 2
    return return_sum

print(amicable_numbers(10000))
