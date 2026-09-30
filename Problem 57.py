from fractions import Fraction

counter = 0
current_num = (1 + Fraction(1/2))
for i in range(1,1001):
    current_num = Fraction(1 + Fraction(1 / (1 + current_num)))
    if len(str(current_num.numerator)) > len(str(current_num.denominator)):
        counter += 1
print(counter)
