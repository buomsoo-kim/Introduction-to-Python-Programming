def checker(word):
    shown = []
    for i in range(len(word)-1):
        if word[i] in shown:
            return False
        if word[i] == word[i+1]:
            pass
        else:
            shown.append(word[i])
    if word[-1] in shown:
        return False
    return True

n = int(input())
words = []
num_group_words = 0
for i in range(n):
    words.append(input())
for word in words:
    if checker(word):
        num_group_words += 1
print(num_group_words)