#A,B 카드 정렬하기
N=int(input())

num_list=[]
for _ in range(N):
    num_list.append(int(input()))

num_list.sort()

sum_list=num_list[0]
all_sum=[]

for i in range(1,N):
    sum_list+=num_list[i]
    all_sum.append(sum_list)

print(sum(all_sum))

