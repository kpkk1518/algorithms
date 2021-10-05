#외벽점검 원형을 -> 일자로 만들어주고 완전 탐색하는 아이디어 필요!
from itertools import permutations
def solution(n,weak,dist):
    length=len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    answer = len(dist)+1 #투입할 친구의 최솟값을 찾아야하므로 MAXIMUM일단 정함.
    for start in range(length):
        #친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist,length)):
            count=1
            #해당 친구가 점검할 수 있는 마지막 위치
            position=weak[start]+friends[count-1]
            #시작점 부터 모든 취약 지점을 확인
            for index in range(start,start+length):
                #점검할 수 있는 위치를 벗어나는 경우
                if position<weak[index]:
                    count+=1
                    if count>len(dist):#친구 투입이 더이상 안된다면
                        break
                    position=weak[index]+friends[count-1]
            answer=min(answer,count)
        if answer>len(dist):
            return -1
    return answer
