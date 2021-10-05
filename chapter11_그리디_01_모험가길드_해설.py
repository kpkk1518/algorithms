#공포도기준오름차순 정렬 수행
n=int(input())
data=list(map(int,input().split()))
data.sort()

count=0 #그룹에 포함된 모험자의 수
result=0 #총 그룹수
for i in data:
    count+=1
    if count>=i:#사람수가 공포도 이상이라면
        count=0
        result+=1
print(result)
    
