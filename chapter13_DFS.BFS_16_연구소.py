from itertools import combinations

n,m=map(int,input().split())

temp=[[0] *m for _ in range(n)]
temp1=list(combinations(temp,3))
data=[]
avaliable_wall=[]
for _ in range(n):
    data.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if data[i][j]==0:
            avaliable_wall.append((i,j))
more=combinations(avaliable_wall,3)
#좌상우하
dx=[-1,0,1,0]
dy=[0,1,0,-1]

result=0

#깊이우선탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        #상,하,좌,우 바이러스가 퍼질 수  있는 경우
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                #해당위치에 바이러스 배치하고 재귀적 수행!
                temp[nx][ny]==2
                virus(nx,ny)

#현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

#깊이 우선탐색(DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
    global result
    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=data[i][j]
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        #안전영역의 최댓값 계산
        result=max(result,get_score())
        return

    for i in range(n):
        for j in range(m):
            if data[i][j]==0:
                data[i][j]==1
                count+=1
                dfs(count)
                data[i][j]=0
                count-=1
dfs(0)
print(result)