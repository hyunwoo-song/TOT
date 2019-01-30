T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    score = [0]*N
    total_score = [0]*N
    count = 0
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for n in range(N):
        score[n] = list(map(int, input().split()))
        total_score[n] = (0.35*score[n][0])+(0.45*score[n][1])+(0.2*score[n][2])
    sorted_total = sorted(total_score)[::-1]
    
    
    for s in sorted_total:
        for index, t_score in enumerate(total_score):
            if s == t_score:
                total_score[index]= grade[0]
                count += 1
                if count >= N/10:
                    count = 0
                    grade.pop(0)

    print(f'#{t+1} {total_score[K-1]}')