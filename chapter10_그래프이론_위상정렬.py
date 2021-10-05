from collections import deque

#노드 개수 ,간선 개수
v,e=map(int,input().split())

#모든 노드에 대한 진입차수는 0
indegree=[0]*(v+1)
#간선정보를 담을 리스트
graph=[[]for _ in range(v+1)]

for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b) #a->b 이동가능
    indegree[b]+=1

#위상정렬 함수
def topology_sort():
    result=[]
    q=deque()
    #진입차수가 0인 노드 넣기
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
        
    while q:
        now=q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)


    for i in result:
        print(i)

topology_sort()

