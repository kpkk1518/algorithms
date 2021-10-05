from itertools import combinations
N,M=map(int,input().split())
balling=list(map(int,input().split()))
#print(combinations(balling,2))
result=[]
for i in combinations(balling,2):
    if i[0]==i[1]:
        continue
    result.append(i)

print(len(result))

