final_list = []
for i in range(100000):
    if "0" in str(i):
        pass
    for j in range(100):
        if "0" in str(j):
            pass
        if (sorted(str(i)+str(j)+str(i*j))) == ["1","2","3","4","5","6","7","8","9"]:
            final_list.append(i*j)
            
print(sum(list(set(final_list))))
