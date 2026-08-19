longest_chain_length = 0
longest_chain_number = 0


for collatz in range(2,1000001):
    collatz_sequence = collatz
    counter = 0
    while collatz_sequence != 1:
        if collatz_sequence == 4:
            counter += 3
            break
        elif collatz_sequence % 2 == 0:
            collatz_sequence = collatz_sequence / 2
            counter += 1
        else:
            collatz_sequence = 3 * collatz_sequence + 1
            counter += 1
    if counter > longest_chain_length:
        longest_chain_length = counter
        longest_chain_number = collatz

print(longest_chain_number)
