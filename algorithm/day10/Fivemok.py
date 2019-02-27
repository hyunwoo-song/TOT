import sys
sys.stdin = open('input.txt' ,'r')


def DFS2(y, x, z, i):
    m = 1
    new_y = y + dy[i]
    new_x = x + dx[i]
    count[i] += 1
    Visited[y][x] = True
    while m < 5:
        m += 1
        new_y += dy[i]
        new_x += dx[i]
        if 0 <= new_y and new_y <= N - 1 and new_x <= N - 1 and 0 <= new_x:
            if Pan[new_y][new_x] == z and not Visited[new_y][new_x]:
                Visited[y][x] = True
                count[i] += 1
            else:
                break
        else:
            break


def DFS(y, x, z):
    global result
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        Visited = [[0] * N for _ in range(N)]
        if 0 <= new_y and new_y <= N - 1 and new_x <= N - 1 and 0 <= new_x:
            if Pan[new_y][new_x] == z and not Visited[new_y][new_x]:
                count[i] += 1
                DFS2(new_y, new_x, z, i)

                if count[i] == 5:
                    result = z
                    R.append(y+1)
                    R.append(x+1)
                    break



    return result

N = 6
Pan = [list(map(int, input().split())) for n in range(N)]
result=0
dy = [0, 1, 1, 1]
dx = [1, 1, 0, -1]
R = []
Visited = [[0] * N for _ in range(N)]
for y in range(N):
    for x in range(N):
        count = [1] * 4
        if Pan[y][x]:
            z = Pan[y][x]
            DFS(y, x, z)
            if result:
                break
if result:
    print(result)
    print(' '.join(map(str, R)))

else:
    print(result)
