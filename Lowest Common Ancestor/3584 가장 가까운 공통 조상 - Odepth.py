'''
3584 가장 가까운 공통 조상 - Linear
시간 제한이 넉넉해서 그냥 가장 쉬운 풀이로 푸는 문제이다.
내가 사용한 방식은 다음과 같다.
우선 부모 자식 사이를 연결해 준다.
이후 원하는 두 노드의 깊이를 조사해서
두 노드가 같은 깊이를 가지도록 부모를 타고 올려보낸다.
거기서부터 하나씩 위로 올라가면서 같은 노드가 나올 때까지 반복한다.
이렇게 했는데 다른 답 보니까 더 쉬운 방법이 있었다.
그냥 두 노드중에 하나 잡아서 루트까지 visited 배열 체크하고
나머지 노드 올리면서 visited 있으면 그거 출력하는 방식이다.
visited 만들 생각을 못 하고 배열 만들어서 저장하면 너무 크겠다 생각만 했다. 
'''
import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n=int(input())
  parent=[0]*(n+1)
  for i in range(n-1):
    a,b=map(int,input().split())
    parent[b]=a
  a,b=map(int,input().split())

  def d(x):
    c=0
    while parent[x]:
      x=parent[x]
      c+=1
    return c

  def d2(x,k):
    for i in range(k):
      x=parent[x]
    return x

  if d(a)>d(b):
    a=d2(a,d(a)-d(b))
  if d(a)<d(b):
    b=d2(b,d(b)-d(a))
    
  def f(x,y):
    while x!=y:
      x=parent[x]
      y=parent[y]
    return x

  print(f(a,b))
