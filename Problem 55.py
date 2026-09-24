def check_palindrome(s):
    if len(s) == 1:
        return False
    l = 0
    r = -1
    for i in range(len(s)//2+1):
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

result = 0
output_list = []
for i in range(1,10000):
    result = i
    for j in range(50):
        result = result + int(str(result)[::-1])
        if check_palindrome(str(result)):
            output_list.append(result)
            break
print(9999-len(output_list))
