def palindrome_checker(n):
    counter = 1
    palindrome_sum = 0
    while counter < n:
        if (str(counter) == str(counter)[::-1]) and (str(bin(counter)[2:]) == str(bin(counter))[-1:1:-1]) :
            palindrome_sum += counter
        counter += 1
    return palindrome_sum

print(palindrome_checker(1000000))
