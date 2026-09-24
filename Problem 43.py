def valid_num_check(num):
    valid_list = []
    for i in range(100,1000):
        if i % num == 0:
            valid_list.append(i)
    return valid_list
def unique_digit_checker(s):
    checker = [i for i in str(s)]
    for a in checker:
        if checker.count(a) > 1:
            return False
    return True
        
divisible_list = [2,3,5,7,11,13,17]
digits = [0,1,2,3,4,5,6,7,8,9]
possible_list = []
end_digits = []
output_list = []
final_sum = 0
for j in range(0, len(divisible_list), 3):
    possible_list.append(valid_num_check(divisible_list[j]))
for a in possible_list[2]:
    for b in possible_list[1]:
        for c in possible_list[0]:
            if unique_digit_checker(str(c)+str(b)+str(a)):
                    end_digits.append(int(str(c)+str(b)+str(a)))
for k in end_digits:
    if "0" not in str(k):
        pass
    for p in digits:
        if str(p) in str(k):
            pass
        else:
            output_list.append(int(str(p)+str(k)))
for q in output_list:
    if int(str(q)[2:5]) % 3 == 0 and int(str(q)[3:6]) % 5 == 0 and int(str(q)[5:8]) % 11 == 0 and int(str(q)[6:9]) % 13 == 0:
        final_sum += q
        
print(final_sum)

