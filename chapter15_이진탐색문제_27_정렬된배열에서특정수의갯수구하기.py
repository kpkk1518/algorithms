N,x=map(int,input().split())
num=list(map(int,input().split()))
count=0
for i in range(N):
    if x==num[i]:
        count+=1
if count==0:count=-1
print(count)