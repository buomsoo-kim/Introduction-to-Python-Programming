n = int(input())
scores = [int(i) for i in input().split()]
max_score = max(scores)
sum = 0
for score in scores:
    sum += (score/max_score)*100
avg = sum/len(scores)
print(avg)