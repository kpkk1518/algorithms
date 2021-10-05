import os
from typing import final
#해설
def is_it_possible(result):
    for x,y,a in result:
        if a==0:#기둥인 경우
            #바닥 위 혹은 보의 한쪽 끝부분 위 혹은 다른 기둥위라면 정상
            if y==0 or [x-1,y,1] in result or [x,y,1] in result or [x,y-1,0] in result:
                continue
            return False
        elif a==1:
            #한쪽 끝부분이 기둥 위 혹은 양쪽 끝부분이 다른보와 동시에 연결이라면 정상
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x+1,y,1] in result and [x-1,y,1] in result):
                continue
            return False
    return True

        #print(x,y)
#직접 만든것
def solution(n, build_frame):
    result = [[0]*n for _ in range(n)]

    columns=[]
    rows=[]
    print(result)
    final_result=[]
    for x,y,a,b in build_frame:
        if b==1:
            final_result.append([x,y,a])
            is_true=is_it_possible(final_result)
            
            if(is_true):
                continue
            else:
                final_result.remove([x,y,a])
            
            '''
            if a==0:#기둥일때,
                if y==0 or (x,y) in rows or (x,y) in columns:#기둥이 바닥위 /보의 끝부분 위/또다른 기둥 위
                    columns.append((x,y))
                    columns.append((x,y+1))
                    final_result.append([x,y,a])
                else:
                    continue
            elif a==1:#보일때,
                if (x,y) in columns or (x+1,y) in columns or ((x,y) in rows and (x+1,y) in rows): 
                    rows.append((x,y))
                    rows.append((x+1,y))
                    final_result.append([x,y,a])
                else:
                    continue
            '''
        if b==0:#삭제시
            if [x,y,a] in final_result:
                final_result.remove([x,y,a])
                isTrue=is_it_possible(final_result)
                if(isTrue):
                    continue
                else:
                    final_result.append([x,y,a])
    final_result.sort()
    '''
            if a==0:#기둥일때,
                rows.remove((x,y))
                rows.remove((x,y+1))
                #기둥과 접점이 있는 보와 기둥 확인
                possible_check_rows=[]
                possible_check_columns=[]
                if (x,y) in rows :
                    possible_check_rows.append((x,y))
                elif (x,y+1) in rows: 
                    possible_check_rows.append((x,y+1))
                if (x,y) in columns :
                    possible_check_columns.append((x,y))
                elif (x,y+1) in columns:
                    possible_check_columns.append((x,y+1))

                if y==0 or (x,y) in rows or (x,y) in columns:#기둥이 바닥위 /보의 끝부분 위/또다른 기둥 위
                    columns.append((x,y))
                    columns.append((x,y+1))
                    final_result.append([x,y,a])
                else:
                    continue
            elif a==1:#보일때,
                if (x,y) in columns or (x+1,y) in columns or ((x,y) in rows and (x+1,y) in rows): 
                    rows.append((x,y))
                    rows.append((x+1,y))
                    final_result.append([x,y,a])
                else:
                    continue
    '''
    return final_result

#solution(5,	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])