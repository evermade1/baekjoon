'''
2252 줄 세우기 - 위상 정렬 
while 사용하기 위해 deque 사용
처음에 진입차수가 0인 노드를 전부 찾아 append해놓고
while 돌리면서 큐가 빌 때까지 반복
어떤 노드를 조사하면 거기에서 이어지는 경로를 지움
지웠을 때 진입차수가 0이 될 수 있으므로 걔네를 다시 append해 줌
이걸 반복하면 답이 완성됨
'''
from collections import deque
n,m=map(int,input().split())
l=[[] for i in range(n+1)] #경로를 저장하는 배열
d=[0]*(n+1) #in-degree (진입차수, 얘한테 들어가는 노드 개수) 를 저장하는 배열
q=deque() #진입차수가 0인 노드부터 넣는 데크 
ans=[] #정답을 저장하는 배열 

for i in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    d[b]+=1

for i in range(1,n+1):
    if d[i]==0:
        q.append(i)

A=[-1]*(n+1)
c=0
while q:
    x=q.popleft()
    ans.append(x)
    A[x]=c
    for i in l[x]:
        d[i]-=1
        if d[i]==0:
            c+=1
            q.append(i)


s=int(input())
for i in range(s):
    a,b=map(int,input().split())
    if A[a]!=-1 and A[b]!=-1:
        if A[a]<A[b]:
            print(-1)
        elif A[a]>A[b]:
            print(1)
        else:
            print(0)
    else:
        print(0)
