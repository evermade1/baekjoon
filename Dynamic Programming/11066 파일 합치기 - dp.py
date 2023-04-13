'''
11066 파일 합치기 - dp
역대 가장 오랜 시간 걸려서 푼 문제다.
처음엔 파일 하나 추가할 때마다 이전 파일까지의 총합과의 관계를 생각해서 했는데
아무리 해도 답이 근접하기만 하고 맞지가 않아서 틀린 방법이라고 생각했다.
다시 생각한 게 j부터 j+i까지의 최솟값을 하나하나 저장하는 방법이다.
2개짜리의 최솟값, 3개짜리 이렇게 가면서 전체의 최솟값을 알아낸다
3중 for문이라 pypy로 겨우 통과하긴 했지만 감동이다. 
'''
import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  d=[[0 for i in range(j+1)] for j in range(n)]
  for i in range(n-1):
    #d[i][i]=l[i]
    d[i+1][i]=l[i]+l[i+1]
  #d[n-1][n-1]=l[n-1]
  for i in range(2,n): #떨어진 거리
    for j in range(n-i): #시작 위치 (j에서 j+i까지)
      c=1e9
      tmp=0
      for k in range(j,j+i):
        c=min(c,d[k][j]+d[j+i][k+1])
        tmp+=l[k]
      d[j+i][j]=c+tmp+l[j+i]
  print(d[n-1][0])
