final_sum = 1
counter = 1
for i in range(3,1003,2):
    final_sum += (4 * (i**2) - 12 * (counter))
    counter += 1
print(final_sum) 
