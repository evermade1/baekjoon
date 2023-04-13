'''
15681 트리와 쿼리 - 트리에서의 dp
visited 함수에 해당 정점을 루트로 하는 서브트리의 정점 개수를 저장한다.
이렇게 visited 함수를 두 가지 용도로 사용하여 메모리를 절약한다.
방법은 k[x]에 1을 더한 뒤 (자기 자신) x에 연결된 정점들에 대해 이를 반복하면
전체 서브트리의 정점 하나당 1씩 더해지며 개수가 나오게 된다.
처음에는 deque를 사용해서 루트를 먼저 넣고 서브트리를 별도의 배열에 저장했는데
이 방법대로 하면 시간초과가 떴다.
아래 방법이 사실 dp를 사용하는 방법이긴 하다. 
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n,r,t=map(int,input().split())
l=[[] for i in range(n+1)] #이어진 정점들 
k=[0]*(n+1) #visited
for i in range(n-1):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)

def dfs(x):
    k[x]+=1
    for i in l[x]:
        if not k[i]:
            k[x]+=dfs(i)
    return k[x]

dfs(r)
    
for i in range(t):
    u=int(input())
    print(k[u])
