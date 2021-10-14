from collections import deque
#인구이동
def people_change(country):
    global calculate
    unit_appear=False
    q=deque()
    for i in range(N):
        for j in range(N):
            q.append((i,j))
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]
    unit=0
    people=0
    unit_pos=[]
    finish=[]
    #동시에 두그룹일때 어떻게 해야할지 고민해보기 입력예시5번
    while(q):
        pos_x,pos_y=q.popleft()
        finish.append([pos_x,pos_y])
        for i in range(4):
            cur_x=pos_x+dx[i]
            cur_y=pos_y+dy[i]
            if [cur_x,cur_y] in finish:
                continue
            if cur_x<N and cur_x>=0 and cur_y<N and cur_y>=0:
                if [cur_x,cur_y] not in q:
                    q.append([cur_x,cur_y])
                dif=abs(country[pos_x][pos_y]-country[cur_x][cur_y])
                if dif>=L and dif<=R:
                    unit_appear=True
                    unit_pos.append((cur_x,cur_y))
                    unit_pos.append((pos_x,pos_y))
                    unit+=1
                    #people=country[pos_x][pos_y]+country[cur_x][cur_y]
    if not unit_appear:
        return country,unit_appear #유닛이 없다.
    #Q가 끝나면
    unit_pos=set(unit_pos)
    #people 계산
    for i in unit_pos:
        people+=country[i[0]][i[1]]
    
    country_per=people//(unit+1)
    for i in unit_pos:
        country[i[0]][i[1]]=country_per
    calculate+=1
    return country,unit_appear



calculate=0
N,L,R = map(int,input().split())
country=[]
for i in range(N):
    country.append(list(map(int,input().split())))

country,is_going=people_change(country)
while(is_going):
    country,is_going=people_change(country)

print(calculate)