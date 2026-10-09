def compute_digit_letter_sum(number_words):
    output_sum = 0
    for i in number_words:
        output_sum += len(i)
    return output_sum


units = ["one","two","three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["twenty","thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
ten_to_twenty = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
hundred = 7
ten = 3
hundred_and = 10
unit_letter_sum = compute_digit_letter_sum(units)
tens_letter_sum = compute_digit_letter_sum(tens)
ten_to_twenty_letter_sum = compute_digit_letter_sum(ten_to_twenty)

final_sum = 0
for i in range(10):
    final_sum += (9*unit_letter_sum)
    final_sum += (10*tens_letter_sum)
    final_sum += ten
    final_sum += ten_to_twenty_letter_sum
    
final_sum += unit_letter_sum * 100

for i in range(9):
    final_sum += hundred_and * 99
    final_sum += hundred
        
final_sum += 11

print(final_sum)
