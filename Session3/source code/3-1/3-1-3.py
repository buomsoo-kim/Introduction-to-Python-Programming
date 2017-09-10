s = input()
koi = 0
ioi = 0
for i in range(len(s) - 2):
    if s[i:i+3] == 'KOI':
       koi += 1
    if s[i:i+3] == 'IOI':
        ioi += 1

print(koi)
print(ioi)