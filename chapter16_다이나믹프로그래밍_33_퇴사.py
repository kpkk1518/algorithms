n=int(input())
t=[]
p=[]
dp=[0]*(n+1)
for _ in range(n):
    time,money=map(int,input().split())
    t.append(time)
    p.append(money)
print(time)
#할 수 있는 경우의 수

max_value=0
for i in range(n-1,-1,-1):
    time=t[i]+i
    #상담이 기간 안에 끝나는 경우
    
    dp[i]=max(p[i]+dp[t[i]+i],max_value)