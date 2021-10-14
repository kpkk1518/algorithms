from itertools import permutations
n=int(input())
number=list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
sentence=[]

for i in range(add):
    sentence.append('+')
for i in range(sub):
    sentence.append('-')
for i in range(mul):
    sentence.append('x')
for i in range(div):
    sentence.append('/')
count=n-1
a=set(list(permutations(sentence,count)))
result=0
all_result=[]
idx=0
for sen in a:
    for idx,j in enumerate(sen):
        if j=='+':
            if idx==0:
                result=number[idx]+number[idx+1]
            else:
                result=result+number[idx+1]
        elif j=='-':
            if idx==0:
                result=number[idx]-number[idx+1]
            else:
                result=result-number[idx+1]
        elif j=='x':
            if idx==0:
                result= number[idx]* number[idx+1]
            else:
                result=result*number[idx+1]
        elif j=='/':
            if idx==0:
                
                if number[idx]<0 and number[idx+1]>0:
                    result=abs(number[idx])//number[idx+1]
                    result= -result
                else:
                    result = number[idx]//number[idx+1]
            else:
                if result<0 and number[idx+1]>0:
                    result=abs(result)//number[idx+1]
                    result= -result
                else:
                    result=result//number[idx+1]
    all_result.append(result)
    result=0

print(max(all_result))
print(min(all_result))


