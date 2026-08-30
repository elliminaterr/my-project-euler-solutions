def fibonacci():
    a = 1
    b = 1
    index = 2
    
    while len(str(b)) < 1000:
        a,b = b,(a+b)
        index += 1
    
    return index
    
print(fibonacci())
