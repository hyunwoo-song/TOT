# N=5
# M=3
# Data_Fuel={}
# for i in range(1,6):
#     Data_Fuel.update({i:1})
# A=[0]*M+1
# def go(now_index):
#     global M
#
#     if now_index==M:
#         print(A)
#         return
#
#     for D in Data_Fuel.keys():
#         if Data_Fuel[D]>0:
#             if(now_index>0):
#                 if(A[now_index-1]==D):
#                     continue
#             A[now_index]=D
#             Data_Fuel[D]=Data_Fuel[D]-1
#             go(now_index+1)
#             Data_Fuel[D] = Data_Fuel[D] + 1
# go(0)


def PMT(depth):
    global M,N
    if depth == M:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i]=True
            result[depth] = l[i]
            PMT(depth +1)
            visited[i]= False


N= 5
M =3
l = [1, 2, 3, 4, 5]
visited=[0]*N
result=[0]*M
PMT(0)



def CBN(depth,idx):
    global M,N
    if depth == M:
        print(result)
        return

    for i in range(idx,N):
        if not visited[i]:
            visited[i]=True
            result[depth] = l[i]
            PMT(depth +1,idx)
            visited[i]= False

N= 5
M =3
l = [1, 2, 3, 4, 5]
visited=[0]*N
result=[0]*M
PMT(0,0)

