#Hint: Look at repeating section of 1/7

for i in range(10000,1000000):
    num_list = [int(x) for x in str(i)]
    num_list_two = [int(x) for x in str(i * 2)]
    num_list_three = [int(x) for x in str(i * 3)]
    num_list_four = [int(x) for x in str(i * 4)]
    num_list_five = [int(x) for x in str(i) * 5]
    num_list_six = [int(x) for x in str(i) * 6]
    
    num_list.sort()
    num_list_two.sort()
    num_list_three.sort()
    num_list_four.sort()
    num_list_five.sort()
    num_list_six.sort()
    
    num_list = list(set(num_list))
    num_list_two = list(set(num_list_two))
    num_list_three = list(set(num_list_three))
    num_list_four = list(set(num_list_four))
    num_list_five = list(set(num_list_five))
    num_list_six = list(set(num_list_six))
    
    if num_list == num_list_two == num_list_three == num_list_four == num_list_five == num_list_six:
        print(i)
        break
