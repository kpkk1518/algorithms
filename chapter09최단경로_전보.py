#N개의 도시, 
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)
n,m,c =map(int,input().split())
#노드 정보를 담는 리스트
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c):
    q=[]
    #초기화
    heapq.heappush(q,(0,c))
    distance[c]=0
    while(q):
        dist,now=heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost=dist+i[1] #현재 거리+다음에 이동하는 거리
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                #그 다음 노드로 가는 거리 및 노드
                heapq.heappush(q,(cost,i[0]))
dijkstra(c)

count=0
max_distance=0 
for i in range(n+1):
    if distance[i]!=INF:
        count+=1
        max_distance=max(distance[i],max_distance)
print(count-1,max_distance)
