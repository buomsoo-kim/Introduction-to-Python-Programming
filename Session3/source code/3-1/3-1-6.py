def score_calculator(result):
    sequence = 1
    score = 0
    for r in result:
        if r == 'O':
            score += sequence
            sequence += 1
        else:
            sequence = 1
    return score

n = int(input())
for i in range(n):
    print(score_calculator(input()))