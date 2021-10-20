# 학생 N명, 국어,영어,수학 
# 국어 점수
N=int(input())
student_list=[]
for _ in range(N):
    student_list.append(list(map(str,input().split())))

for each_student in student_list:
    each_student[1]=int(each_student[1])
    each_student[2]=int(each_student[2])
    each_student[3]=int(each_student[3])

student_list.sort(key = lambda x :(-x[1],x[2],-x[3],x[0]))

