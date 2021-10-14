from collections import deque

n=int(input())
arr=[]

for _ in range(n):
    arr.append(list(map(str,input().split())))

arr_num=[[0]*n for _ in range(n)]
num_wall=0
'''
for i in range(n):
    for j in range(n):
        
        if arr[i][j]=='X':
            continue
        elif arr[i][j]=='S':
            arr_num[i][j]=1
        elif arr[i][j]=='T':
            arr_num[i][j]=2
'''

def find_student(arr):
    student_arr=[]
    teacher_arr=[]
    teacher_arr=deque()
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='S':
                student_arr.append((i,j))
            elif arr[i][j]=='T':
                teacher_arr.append((i,j))
    dx=[0,0,1,-1]
    dy=[-1,1,0,0]
    dz=['down','up','right','left']
    find_student=False
    
    while (teacher_arr): #선생님 확인
        go_through=True
        pos_y,pos_x=teacher_arr.popleft()
        for i in range(4): #상하좌우 확인
            while(go_through):
                search_x=pos_x+dx[i]
                search_y=pos_y+dy[i]
                if dz[i]=='down':
                    if search_y==n:break
                elif dz[i]=='up':
                    if search_y<0:break
                elif dz[i]=='right':
                    if search_x==n:break
                elif dz[i]=='left':
                    if search_x<0: break
                if arr[search_y][search_x]=='S':
                    find_student=True
                    return find_student
                elif arr[search_y][search_x]=='T' or arr[search_y][search_x]=='O':
                    go_through=False

    return find_student


def dfs(count):
    global num_wall
    #벽이 3개이면
    if count==3:
        is_student=find_student(arr)
        if is_student==False:
            return False
    #감시 빈공간에 벽 채우기
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='X':
                arr[i][j]=='O'
                count+=1
                dfs(count)
                arr[i][j]=='X'
                count-=1
    return True

print(dfs(0))