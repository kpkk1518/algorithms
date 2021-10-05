data=input()
sum=0
sum_en=[]
for i in data:
    try:
        sum+=int(i)
    except:
        sum_en.append(i)
sum_en.sort()
result=''
for i in sum_en:
    result+=i
result+=str(sum)
print(result)