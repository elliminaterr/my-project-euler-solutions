LARGEST_CHAIN = 59
final_counter = 0
factorial_list = [1,1,2,6,24,120,720,5040,40320,362880]
for i in range(1,1000000):
    loop_count = 1
    loop_continue = True
    num = i
    while loop_continue:
        num = sum([factorial_list[int(a)] for a in str(num)])
        if num == 169:
            loop_count += 2
            loop_continue = False
        elif num == 871 or num == 872:
            loop_count += 1
            loop_continue = False
        elif num == 145 or num == 40585 or num == 2 or num == 1:
            loop_continue = False
        else:
            loop_count += 1
    if loop_count == LARGEST_CHAIN:
        final_counter += 1

print(final_counter)
