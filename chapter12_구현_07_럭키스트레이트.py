data=input()
pivot=int(len(data)/2)
left=data[:pivot]
right=data[pivot:]
sum_left=0
sum_right=0
for idx,idx2 in zip(left,right):
    sum_left+=int(idx)
    sum_right+=int(idx2)

if sum_left==sum_right:
    print('LUCKY')
else:
    print('READY')