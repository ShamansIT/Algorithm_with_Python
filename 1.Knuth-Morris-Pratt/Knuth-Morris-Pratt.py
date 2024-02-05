textFind = "asasad"  # Fragment text for finding

# Create Pi array code agorithm for finding text
pArr = [0] * len(textFind)
j = 0
i = 1

while i < len(textFind):
    if textFind[j] == textFind[i]:
        pArr[i] = j + 1
        i += 1
        j += 1
    else:
        if j == 0:
            pArr[i] = 0
            i += 1
        else:
            j = pArr[j-1]


textSearch = "asasawd asasadwsa"  # Text in which the fragment will be searched

m = len(textFind)
n = len(textSearch)

i = 0
j = 0

# Searching algorithm
while i < n:
    if textSearch[i] == textFind[j]:
        i += 1
        j += 1
        if j == m:
            print(
                f"Fragment exist in text. Start from index [{i-len(textFind)}] to [{i}]")
            break
    else:
        if j > 0:
            j = pArr[j-1]
        else:
            i += 1

if i == n:
    print("Fragment not found")
