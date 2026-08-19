a = 1
b = 2
numbers = [a,b]
temp = 0
total = 0
while temp < 40000000000:
    temp = a + b
    numbers.append(temp)
    a = b
    b = temp
    
for i in range(len(numbers)):
    if len(str(numbers[i])) == 1000:
        print(numbers[i])
        break

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        total += numbers[i]
print(total)
