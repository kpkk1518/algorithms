#이문제는 시간이 적게 걸리는 음식부터 확인하는 탐욕적 접근 방식
#모든 음식을 시간을 기준으로 정렬한 뒤에 적게 걸리는 음식부터 제거해 나가는 방식 우선순위 큐
#정확성: 38.8 효율성: 57.1 합계: 96.0 / 100.0
import heapq
def solution(food_times,k):
    
    if sum(food_times)<k:
        return -1
    
    #시간이 적은 음식부터
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))
        #(음식시간, 음식번호) 순으로 삽입
    
    sum_values=0# 먹기 위해 사용한 시간
    previous=0#직전에 다먹은 음식 시간

    length=len(food_times)#남은 음식의 갯수

    # 먹기 위해 사용한 시간 + (현재 음식 시간-이전의 음식시간)*현재음식 개수와 k 비교
    while sum_values + (q[0][0]-previous)*length<=k:
        now =heapq.heappop(q)[0]
        sum_values +=(now-previous) * length
        length-=1
        previous=now #이전의 음식 시간

    #남은 음식 중에서 몇번째 음식인지 확인
    result=sorted(q,key=lambda x:x[1])
    return result[(k-sum_values)%length][1]


print(solution([3, 1, 2],5))