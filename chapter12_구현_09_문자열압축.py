#
data=input()

result_str=[]
result_num=[]
for i in range(1,len(data)):
    result=[]
    num=1
    for idx,chr in zip(range(0,len(data),i),data):
        pivot=data[idx:idx+i]
        if idx>len(data)-i:
            continue
        if pivot==data[idx+i:idx+(2*i)]:
            num+=1
        else:
            if num==1:
                result.append(pivot)
            else:
                result.append(str(num)+pivot)
            num=1
    tmp=''
    for i in result:
        tmp+=i
    result_str.append(tmp)
    result_num.append(len(tmp))
print(min(result_num))