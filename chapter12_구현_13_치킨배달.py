

#치킨집과 도시의 거리 구하는 법
def getDistance(candidates,house):
    minDis=(1e9)
    min_sum=0 #
    all_sum=[]
    for chicken in candidates:
        min_sum=0
        for hx,hy in house:
            
            minDis=(1e9)
            for cx,cy in chicken:
                temp=abs(cx-hx)+abs(cy-hy)
                if temp<minDis:
                    minDis=temp
            #min_each_house.append(temp)#각 치킨-집간의 최단거리
            min_sum+=minDis#모든 집 치킨-집간의 최단거리의 합
        all_sum.append(min_sum)#치킨집에 따른 집간의 최단거리 합list
    return min(all_sum)

N,M =map(int,input().split())

city=[]

for _ in range(N):
    city.append( list(map(int,input().split()))) 

#조합 사용하기
from itertools import combinations

chicken =[]
house=[]
for i in range(len(city)):
    for j in range(len(city[0])):
        if city[i][j]==1:
            house.append([i+1,j+1])
        if city[i][j]==2:
            chicken.append([i+1,j+1])

#모든 치킨 집 중에 M개를 뽑는 조합 계산
candidiates=list(combinations(chicken,M))
minDis=getDistance(candidiates,house)
print(minDis)
