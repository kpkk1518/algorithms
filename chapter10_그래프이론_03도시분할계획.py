def find_parents(parent,x):
    if parent[x]!=x:
        parent[x]=find_parents(parent,parent[x])
    return parent[x]

def union_parents(parent,a,b):
    a=find_parents(parent,a)
    b=find_parents(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

#노드 개수와 간선
v,e=map(int,input().split())
parent= [0]*(v+1)

#모든 간선을 담을 변수
edges=[]
result=0
#처음 초기화
for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

#가장 비용이 큰 가선
last=0

for edge in edges:
    cost,a,b = edge
    #사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parents(parent,a)!=find_parents(parent,b):
        union_parents(parent,a,b)
        result+=cost
        last=cost

#한 사이클만 그려지게 만들어 놓은 후, 가장 큰 비용을 제거하면 모든 점을 잇는 선이 있지만 사이클이 없는  신장트리가 된다.
print(result-cost)
print(result)
