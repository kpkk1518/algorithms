# 도현이의 집 N  집의좌표 x1,x2,x3,....xn
N,C = map(int,input().split())
num=[]
for _ in range(N):
    num.append(int(input()))
num.sort() #이진 탐색 수행을 위해 정렬
start=num[1]-num[0] #집의 좌표중에 가장 작은 값(최소갭)
end=num[-1]-num[0]# 최대갭
result=0

while(start<=end):
    mid=(start+end)//2 #가장 인접한 두 공유기 사이의 거리 gap
    value=num[0]
    count=1
    for i in range(1,N):
        if num[i]>=value+mid:
            value=num[i]
            count+=1
        if count>=C: # C개 이상의 공유기를 설치할 수 있는 경우
            start = mid+1
            result = mid #최적의 결과 저장
        else:#C개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
            end=mid-1
print(result)
