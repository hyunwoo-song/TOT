import sys
sys.stdin = open('2606.txt')

Com_N = int(input())
Link_N = int(input())
Mymap=[[0x7FFFFFFF]*(Com_N+1) for n in range(Com_N+1)]
for n in range(Link_N):
    m, s = map(int,input().split())
    result = s
    if s > m:
        result = m
    Mymap[m][s] = result
    Mymap[s][m] = result


for via in range(1,Com_N+1):
    for start in range(1,Com_N+1):
        if start != via:
            for stop in range(1,Com_N + 1):
                if start != stop and via != stop:
                    if Mymap[start][stop] >Mymap[start][via] + Mymap[via][stop]:
                        Mymap[start][stop] = min (Mymap[start][via] , Mymap[via][stop])
print(Mymap[1].count(1))


