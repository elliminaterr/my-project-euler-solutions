counter = 0
for a in range(1,50):
    for b in range(1,50):
        if len(str(a**b)) == b:
            counter += 1
print(counter)
