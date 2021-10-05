def find_parents(parent,x):
    if parent[x]!=x:
        parent[x]=find_parents(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parents(parent,a)
    b = find_parents(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


n,m=map(int,input().split())
#노드 갯수
parent=[0]*(n+1)
#처음엔 부모가 자기자신으로 초기화
for i in range(0,n+1):
    parent[i]=i

#각 연산을 하나씩 확인
for i in range(m):
    oper,a,b=map(int,input().split())
    if oper==1:
        if find_parents(parent,a)==find_parents(parent,b):
            print("YES")
        else:
            print("NO")

    elif oper==0:
        union_parent(parent,a,b)

    

