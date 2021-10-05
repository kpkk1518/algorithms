def solution(food_times, k):
    time=0

    while (True):
        for idx,i in enumerate(food_times):
            if i==0:
                continue
            
            food_times[idx]=i-1
            time+=1
            if time==k+1:
                return idx+1
#정확성 중 3개는 시간초과...
# 효율성 0%이다...정확성: 37.5 효율성: 0.0 합계: 37.5 / 100.0
print(solution([3, 1, 2],5))