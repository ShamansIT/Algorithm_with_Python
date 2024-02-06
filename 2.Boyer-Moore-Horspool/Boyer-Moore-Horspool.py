"""
Boyer-Moore-Horspool Algorithm.
An optimization of the Boyer-Moore algorithm, the Boyer-Moore-Horspool 
algorithm is renowned for its efficiency in practical string search scenarios. 
It simplifies the original algorithm by using a bad-character shift of the 
rightmost character of the window to improve average-case time complexity, 
particularly for long search strings.
"""

# Created by: Serhii Spitsyn

text_fragment = "stand"
text_search_in = "Why you should understand this algorithm!"

# Stage 1: generating a table of offsets
symbol_unique = set()  # unique symbol
num_symbol = len(text_fragment)  # number of symbol in image
dict_offsets = {}  # dictionary of offsets

for i in range(num_symbol-2, -1, -1):  # iterational from last symbol
    if text_fragment[i] not in symbol_unique:
        dict_offsets[text_fragment[i]] = num_symbol - i - 1
        symbol_unique.add(text_fragment[i])

if text_fragment[num_symbol-1] is not symbol_unique:  # format for last symbol
    dict_offsets[text_fragment[num_symbol-1]] = num_symbol

dict_offsets['*'] = num_symbol  # offsets for other symbol

# print(dict_offsets)

# Stage 2: fragment search
num_symbol_in = len(text_search_in)

if num_symbol_in >= num_symbol:
    counter = num_symbol-1  # element being checked counter

    while (counter < num_symbol_in):
        k = 0
        for j in range(num_symbol-1, -1, -1):
            if text_search_in[counter-k] != text_fragment[j]:
                if j == num_symbol - 1:
                    # offset if not equal to the last character of the image
                    offset = dict_offsets[text_search_in[counter]] if dict_offsets.get(
                        text_search_in[counter], False) else dict_offsets['*']
                else:
                    offset = dict_offsets[text_fragment[j]]
                counter += offset  # offset string counter
                break
            k += 1
        if j == 0:
            print(f"Fragment found by index {counter-k+1}")
            break
    else:
        print("Fragment NOT found")
