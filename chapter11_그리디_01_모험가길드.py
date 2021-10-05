n = int(input())
#for _ in range(n):
info = map(int,input().split())
horrable=0
count_people=0
count_all=0
for i in info:
    count_people+=1
    if i>horrable:
        horrable=i
    if horrable<=count_people:
        count_people=0
        horrable=0
        count_all+=1
print(count_all)
    
    #공포도 > 사람수
