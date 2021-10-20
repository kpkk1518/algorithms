#해답참고
n=int(input())
dp=[]

for _ in range(n):
    dp.append(list(map(int,input().split())))

#다이나믹 프로그래밍 두번째 줄 부터 내려가면서 확인
for i in range(1,n):
    for j in range(i+1):
        #왼쪽 위에서 내려오는 경우
        if j==0: #왼쪽위가 없는경우
            up_left=0
        else:
            up_left=dp[i-1][j-1]
        #바로 위에서 내려오는는 경우
        if j==i:
            #바로 위가 없는 경우
            up=0
        else :
            up=dp[i-1][j]
        #최대 합을 저장
        dp[i][j]=dp[i][j]+max(up_left,up)
print(max(dp[n-1]))

