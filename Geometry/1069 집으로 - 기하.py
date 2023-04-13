'''
1069 집으로 - 기하
점프보다 거리가 짧은 경우 그냥 걸어가는 것, 넘어갔다가 걸어오는 것, 돌아서 점프해서 오는 것
거리가 긴 경우 그냥 걸어가는 것, 조금 돌아가는 것, 조금 남기고 걸어가는 것
이렇게 각각 세 가지 경우 중 가장 짧게 걸리는 방법을 선택하면 된다.
'''
import sys
input=sys.stdin.readline
x,y,d,t=map(int,input().split())
k=(x**2+y**2)**(1/2)
if k<d:
  ans=min(t+d-k,2*t,k)
else:
  ans=min((k//d+1)*t,k//d*t+k%d,k)
print(ans)
