from fractions import Fraction

num_list = []
for x in range(11,100):
    for y in range(11,100):
        if (int(str(y)[1])) != 0 and int(str(x)[1])==(int(str(y)[0])) and y % 11 != 0:
            if (x/y) == (int(str(x)[0])/(int(str(y)[1]))) and (y > x):
                num_list.append((x,y))

numerator = 1
denominator = 1 
for i in num_list:
    numerator *= i[0]
    denominator *= i[1]

print(Fraction(numerator/denominator).limit_denominator())
