'''
1167 트리의 지름 - 트리
트리의 지름을 구하는 알고리즘이 존재한다.
1) 트리에서 아무 정점이나 정한다.
2) 이 정점 x에서 가장 멀리 떨어져있는 y를 찾는다.
3) y에서 가장 멀리 떨어져있는 z를 찾는다.
4) y에서 z까지의 거리가 트리의 지름이다.
멀리 떨어져있는 정점을 찾는 방법으로 dfs 이외에 다익스트라도 가능하다. 시간은 비슷하다.
sys.stdin.readline을 사용해야 시간 초과가 나지 않는다.
'''
import sys
import heapq
input=sys.stdin.readline
n=int(input())
g=[]
for i in range(n+1):
  g.append([])
for i in range(n):
  k=list(map(int,input().split()))
  a=k.pop(0)
  for j in range(0,len(k)-1,2):
    g[a].append((k[j+1],k[j])) #(거리,정점)

v=[0]*(n+1)
M=0
ans=0
def dfs(x,k):
    global M, ans
    v[x]=1
    for a,b in g[x]:
        if not v[b]:
            dfs(b,k+a)
    v[x]=0
    if k>M:
        ans=x
        M=k
    
dfs(1,0)
tmp=ans
M,ans=0,0
dfs(tmp,0)
print(M)
