decimal = ""
for i in range(1,200000):
    decimal += str(i)
print(int(decimal[0]) * int(decimal[9]) * int(decimal[99]) * int(decimal[999]) * int(decimal[9999]) * int(decimal[99999]) * int(decimal[999999]))

