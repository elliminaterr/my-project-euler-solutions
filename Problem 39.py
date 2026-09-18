from collections import Counter
c = 0
perimeters = []
for a in range(1,998):
    for b in range(2,999):
        c = (a**2 + b**2) ** (1/2)
        p = a + b + c
        if p < 1001 and (p % 1 == 0):
            perimeters.append(p)
print(max(Counter(perimeters).items(), key=lambda k: k[1])[0])
