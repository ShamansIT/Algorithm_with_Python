text_find = "asasad"  # Fragment text for finding

# Create Pi array code agorithm for finding text
pArr = [0] * len(text_find)
j = 0
i = 1

while i < len(text_find):
    if text_find[j] == text_find[i]:
        pArr[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            pArr[i] = 0
            i += 1
        else:
            j = pArr[j-1]


text_search = "asasawd asasadwsa"  # Text in which the fragment will be searched

m = len(text_find)
n = len(text_search)

i = 0
j = 0

# Searching algorithm
while i < n:
    if text_search[i] == text_find[j]:
        i += 1
        j += 1
        if j == m:
            print(
                f"Fragment exist in text. Start from index [{i-len(text_find)}] to [{i}]")
            break
    else:
        if j > 0:
            j = pArr[j-1]
        else:
            i += 1

if i == n:
    print("Fragment not found")
