from decimal import *
import math
getcontext().prec = 102
total_digit_sum = 0
for i in range(2,101):
    if not math.sqrt(i) % 1 == 0:
        total_digit_sum += sum(int(x) for x in str((Decimal(i).sqrt())).replace('.', '')[:100])
print(total_digit_sum)
