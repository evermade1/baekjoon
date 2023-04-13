'''
백준 13549 숨바꼭질 3 - bfs
숨바꼭질 4에서 다 설명했지만 다른 점이 있고 맨날 까먹어서 다시 쓴다.
시간 관리를 위해 양방향 큐인 deque를 사용한다.
이 문제에서는 다른 숨바꼭질 문제와는 다르게 순간이동과 걷는 것의
소요 시간이 다르기 때문에 조금 다르게 풀어야 한다.
순간이동의 소요시간이 짧기 때문에 순간이동시 값의 우선순위를 올려야 한다.
다 풀고 정답 확인했더니 순간이동은 appendleft로 앞으로 보내던데,
난 그냥 순간이동시의 조건문을 먼저 써서 해결했다.
deque를 사용한 걸 생각하면 전자가 맞는 방법인 것 같다.
'''

from collections import deque
n,k=map(int,input().split())
l=[-1]*100001
l[n]=0
q=deque()
q.append(n)

while q:
    x=q.popleft()
    if x==k:
        print(l[k])
        break
    if 2*x<100001 and l[2*x]==-1:
        l[2*x]=l[x]
        q.append(2*x)
    if 0<=x-1 and l[x-1]==-1:
        l[x-1]=l[x]+1
        q.append(x-1)
    if x+1<100001 and l[x+1]==-1:
        l[x+1]=l[x]+1
        q.append(x+1)

