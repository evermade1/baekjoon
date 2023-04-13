'''
4803 트리 - dfs
골드 4 문젠데 훨씬 어려운 것 같다. 트리중에 가장 나중에 풀었다.
전체 연결 요소를 받아서 트리의 개수를 리턴하는 문제다.
visited 배열의 사용이 상당히 중요하다.
dfs를 돌 때 필연적으로 a에서 b로 갔으면 b에서 a로도 올 수 있으므로 이를 일단 막는다.
이후 visited 배열을 체크해 가면서 이미 방문한 노드를 또 왔다면 사이클이므로
트리의 개수에서 제외한다.
노드 하나하나 dfs를 돌리는데, 방문하지 않은 노드에 한해서만 돌린다.
마지막 출력 형식도 좀 귀찮았다. 

'''
import sys
input=sys.stdin.readline

def dfs(p,x):
  if v[x]==1:
    ans[0]=1
    return
  v[x]=1
  for i in d[x]:
    if i!=p:
      dfs(x,i)

c=0
while True:
  c+=1
  n,m=map(int,input().split())
  if n==0:
    break
  d=[[] for i in range(n+1)]
  v=[0]*(n+1)
  ans=[0]
  for i in range(m):
    a,b=map(int,input().split())
    d[a].append(b)
    d[b].append(a)
  t=0
  for j in range(1,n+1):
    if v[j]==0:
      t+=1
      dfs(j,j)
      if ans[0]==1:
        t-=1
        ans[0]=0
  print('Case ',c,': ',sep='',end='')
  if t>1:
    print('A forest of',t,'trees.')
  elif t==1:
    print('There is one tree.')
  else:
    print('No trees.')
    
