def is_allright(p):
    count=0

    for idx,i in enumerate(p):
        if i=='(':
            
            count+=1
        elif i==')':
            
            count-=1
        if count<0:
            return False
    if count==0:
        return True

def recursion(p):
    if(is_allright(p)):
        return -1
    start=0
    end=0
    for idx,i in enumerate(p):
        if i=='(':
            start+=1
        elif i==')':
            end+=1
        if start==end:
            pivot=idx
            return pivot




def solution(p):
    answer=''
    if p=='':
        return answer
    
    pivot=0
    if is_allright(p)==True:
        return p
    pivot=recursion(p)
    

    u=p[:pivot+1]#균형잡힌 문자열
    v=p[pivot+1:]#나머지

    #빈문자면 빈문자 반환
    
    #올바른 괄호 문자열이면 v에 대한 함수를 수행한 결과를 붙여 반환
    if is_allright(u):
        answer=u+solution(v)
        return answer

    else:
        answer = '('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1])
    
        for idx,i in enumerate(u):
            if i=='(': 
                u[idx]=')'
            elif i==')':
                u[idx]='('
        answer+="".join(u)##리스트를 String으로 붙일때!
        return answer



#print(solution('(()())()'))
#print(solution(')('))
print(solution("()))((()"))