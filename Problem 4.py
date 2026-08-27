num = 993
products= []
temp = 0
num2 = 900
for i in range(100):
    temp = num * num2
    products.append(temp)
    num2 += 1

for x in range(len(products)):
    if str(products[x]) == str(products[x])[len(str((products[x])))::-1]:
        temp = products[x]
        
print(temp)
