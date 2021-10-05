#chapter11_그리디_02_곱하기_혹은_더하기.py
data = input()
result=1
for i in data:
    if int(i)==0:
        continue
    else:
        result*=int(i)

print(result)