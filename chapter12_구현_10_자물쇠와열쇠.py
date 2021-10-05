def rotate_a_matrix_by_90_degree(a):
    n=len(a)#행길이
    m=len(a[0])#열길이
    result =[[0]*n for _ in range(m)]#행 m 열 n인 2차원 배열
    for i in range(n):
        for j in range(m):
            result[j][n-1-i]=result[i][j]

    return result

def check(new_lock):
    is_true=True
    lock_length=len(new_lock) 
    for i in range(lock_length,2*lock_length):
        for j in range(lock_length,2*lock_length):
            if new_lock[i][j]!=1:
                is_true=False
                return is_true
    return is_true

def solution(key,lock):
    n=len(lock)
    m=len(key)
    new_lock=[[0]*(3*n) for _ in range(3*n)]
    for i in range(lock):
        for j in range(lock[i]):
            new_lock[n+i][n+j]=lock[i][j]
    
    for _ in range(4):
        
        key=rotate_a_matrix_by_90_degree(key)
        for x in range(2*n):
            for y in range(2*n):

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                
                if check(new_lock)==True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]

    return False
                

            

    