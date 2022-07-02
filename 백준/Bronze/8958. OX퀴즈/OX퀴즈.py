n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0
    score_sum = 0
    for ox in ox_list:
        if ox == "O":
            score += 1
            score_sum += score
        else:
            score = 0
    print(score_sum)