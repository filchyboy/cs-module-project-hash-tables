# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

alphakey = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

with open("ciphertext.txt") as f:
    copy = f.read()

count_characters = {}
for char in copy:
## if alphakey
    if char in count_characters:
        count_characters[char] += 1
    elif char.isalpha() and char not in count_characters:
## or give 1 as alphakey
        count_characters[char] = 1

# do a sort on the dictionary
order_count = [char[0] for char in sorted(count_characters.items(), key=lambda x: x[1], reverse=True)]

# convert to array
text_chars = list(copy)

# develop the load
decoded_str = [None] * len(text_chars)

for i in range(len(order_count) - 1):
    for j in range(len(text_chars)):
        if text_chars[j] == order_count[i]:
            decoded_str[j] = alphakey[i]
        elif decoded_str[j] is None:
            decoded_str[j] = text_chars[j]

print("".join(decoded_str))