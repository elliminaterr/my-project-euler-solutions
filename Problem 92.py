counter = 0
for num in range(1,10000000):
    solved = False
    square_sum = num
    while not(solved):
        square_sum = sum([int(i)**2 for i in str(square_sum)])
        if square_sum == 89:
            solved = True
            counter += 1
        elif square_sum == 1:
            solved = True
            
print(counter)
