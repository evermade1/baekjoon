'''
11758 CCW - CCW, 기하
CCW를 알아야 풀 수 있는 아주 이기적인 문제다.
외적을 이용해서 구하는 삼각형의 면적은 아래 a에 절댓값 씌우고 1/2한 값인데,
절댓값 씌우기 전 값이 양수이면 반시계, 0이면 일직선, 음수이면 시계방향이다.
'''
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
a=x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
if a>0:
  print(1)
elif a==0:
  print(0)
else:
  print(-1)
