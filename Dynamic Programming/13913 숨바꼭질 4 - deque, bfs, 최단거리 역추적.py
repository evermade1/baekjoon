'''
13913 숨바꼭질 4 - deque, bfs, 최단거리 역추적
맨날 이 유형 풀 때마다 해매서 그냥 쓴다.
배열로 하면 시간초과 나서 데크로 해야 한다.
bfs를 사용하기 때문에 같은 위치에 도착하더라도 나중에 도착한 애는 무조건 느리다.
그래서 그냥 해당 위치 방문 유무만 확인하면 된다.
주의할 점은 n이랑 k가 같으면 오류가 나서 따로 분류해 주어야 하고,
n이 0이면 배열 d를 0으로 초기화했을 경우 메모리 초과가 나기 때문에
배열 d는 -1로 초기화해주어야 한다. 
'''
import sys
from collections import deque
n,k=map(int,input().split())
if n==k:
    print(0)
    print(n)
    exit(0)
d=[-1]*100002
q=deque()
q.append(n)

ans=[]
def f(x):
    c=0
    while x!=n:
        ans.append(x)
        x=d[x]
    ans.append(n)
    ans.reverse()
    print(len(ans)-1)
    print(*ans)
    
while q:
    x=q.popleft()
    if x==k:
        f(k)
    for i in (x-1,x+1,x*2):
        if 0<=i<=100001:
            if d[i]==-1:
                d[i]=x
                q.append(i)
