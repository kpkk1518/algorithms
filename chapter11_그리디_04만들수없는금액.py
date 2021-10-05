from itertools import combinations

N=int(input())
coin_idx=list(map(int,input().split()))
coin_idx.sort()
avaliable_coin=[]
for idx in range(1,len(coin_idx)+1):
    for i in combinations(coin_idx,idx):
        sum=0
        for j in i:
            sum+=j
        avaliable_coin.append(sum)

result_av=set(avaliable_coin)
ava_max=max(result_av)+1

for i in range(1,ava_max+1):
    if i not in result_av:
        print(i)
        break




