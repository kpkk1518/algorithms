
#모든 간선의 비용이 동일할때는 BFS 사용
#특정한도시 X를 시작점-> BFS수행
from collections import deque
n ,m ,k,x=map(int,input().split())
graph=[[] for _ in range(n+1)]
#모든 도로 정보 입력 받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

#모든 도시에 대한 최단거리 초기화
distance = [-1]*(n-1)
distance[x]=0 #출발 도시까지의 거리는 0
#BFS 수행
q=deque([x])

while q:
    now=q.popleft()
    for next_node in graph[now]:
        #아직 방문하지 않은 도시
        if distance[next_node]==-1:
            #최단거리 갱신
            distance[next_node]=distance[now]+1
            q.append(next_node)

#최단거리가 K인 모든 도시의 번호를 오름차순으로 출력
check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)
