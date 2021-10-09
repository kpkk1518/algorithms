from collections import deque 
n,k=map(int,input().split())
result=[[0]*n for _ in range(n)]
position=[]
for _ in range(n):
    subposition=list(map(int,input().split()))
    #result[x][y]=virus
    position.append(subposition)
s,x,y=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=deque()
time_arr=[[100]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if position[i][j]!=0:
            q.append((i,j,0))#0초일때
            time_arr[i][j]=0
while q:
    ii,jj,time=q.popleft()
    if time>=s:
        break          
    virus=position[ii][jj]
    for z in range(4):
        if ii+dx[z]>=0 and ii+dx[z]<n and jj+dy[z]>=0 and jj+dy[z]<n: 
            if position[ii+dx[z]][jj+dy[z]]==0:
                position[ii+dx[z]][jj+dy[z]]=virus
                q.append((ii+dx[z],jj+dy[z],time+1))
                time_arr[ii+dx[z]][jj+dy[z]]=time+1
            elif position[ii+dx[z]][jj+dy[z]]!=0:
                if time_arr[ii+dx[z]][jj+dy[z]]<time+1:
                    continue
                if time_arr[ii+dx[z]][jj+dy[z]]==time+1:
                    position[ii+dx[z]][jj+dy[z]]=min(position[ii+dx[z]][jj+dy[z]],virus)
                    q.append((ii+dx[z],jj+dy[z],time+1))
                    time_arr[ii+dx[z]][jj+dy[z]]=time+1
print(position[x-1][y-1])