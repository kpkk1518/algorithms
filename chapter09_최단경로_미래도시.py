#import pandas as pd
n,m=map(int,input().split())
INF=int(1e9)
#2차원 리스트
graph=[[INF]*(n+1) for _ in range(n+1) ]
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

x,k=map(int,input().split())
#1번->K번 ->X번
'''

for idx in range(2,n+1):
    graph[1][k]=min(graph[1][k],graph[1][idx]+graph[idx][k])
for idx in range(1,n+1):
    graph[k][x]=min(graph[k][x],graph[k][idx]+graph[idx][x])

'''

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[i][j])




if graph[1][k]+graph[k][x]>=INF:
    print(-1)

else:
    print(graph[1][k]+graph[k][x])
    