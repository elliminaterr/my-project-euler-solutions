def generate_triangle_numbers(n):
    num_sum = 0
    output_list = []
    for i in range(1,n+1):
        num_sum += i
        output_list.append(num_sum)
    return output_list

comparision_list = generate_triangle_numbers(100)
final_sum = 0
word_values = []

with open("0042_words.txt") as f:
    x = f.readline()
words_list = x.split(",")
words_list = [k[1:-1] for k in words_list]
for i in words_list:
    word_value = 0
    for j in i:
        word_value += ord(j) - 64
    word_values.append(word_value)

for a in range(len(word_values)):
    if word_values[a] in comparision_list:
        final_sum += 1
print(final_sum) 
