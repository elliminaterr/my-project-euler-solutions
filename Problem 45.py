def generate_triangular_number(n):
    return ((n+1) * n) / 2

def generate_pentagonal_number(n):
    return (n * ((3 * n) - 1)) / 2
    
def generate_hexagonal_number(n):
    return n * ((2 * n) - 1)

triangular_list = []
pentagonal_list = []
hexagonal_list = []
for i in range(286, 100000):
    triangular_list.append(generate_triangular_number(i))
    pentagonal_list.append(generate_pentagonal_number(i))
    hexagonal_list.append(generate_hexagonal_number(i))
    
for i in triangular_list:
    if i in pentagonal_list and i in hexagonal_list:
        print(i)
        break
