
n=str(input())

#for k in range(len(n)):
zero_idx=[]
one_idx=[]
for idx,i in enumerate(n):
    i=int(i)
    if i==0:
        zero_idx.append(idx)
    elif i==1:
        one_idx.append(idx)

zero_cnt=0
one_cnt=0
now=0
#0011001100
for idx in enumerate(len(zero_idx)-1):
    if zero_idx[idx]+1!=zero_idx[idx+1]:
        zero_cnt+=1

for idx in enumerate(len(one_idx)-1):
    if one_idx[idx]+1!=one_idx[idx+1]:
        one_cnt+=1

if zero_cnt>one_cnt:
    cal=0
    cal_op=1
else:
    cal=1
    cal_op=0

result=[]
for i in range(n):
    i=int(i)
    if cal==i:
        i=cal_op
    result.append(i)

#정답봄..






    