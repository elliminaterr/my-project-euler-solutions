numbers = []
multiples = []
total = 0

for i in range(1000):
    numbers.append(i)
    if (i % 3 == 0) or (i % 5 == 0):
        multiples.append(i)

for x in range(len(multiples)):
    total += multiples[x]
    
print(total)
