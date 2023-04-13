'''
11438 LCA 2 - 최소 공통 조상, Sparse Table
LCA 1번과는 주어진 시간이 다르기 때문에 sparse table을 사용하여야 하는 문제다.
a,b의 깊이를 맞추는 데 한 번, LCA를 구하는 데 한 번 사용한다.
나머지는 다 이해가 갔는데 LCA 구하는 식이 이해가 안 됐었다.
밑에 주황색 주석으로 설명해 놓았다.
폰 노이만 무한급수 문제처럼 위아래로 왔다갔다 하면서 정답에 가까워지는 방식이다.
저번 근무 때 풀고 퇴근하고 싶었는데 이해가 안 돼서 오늘 오자마자 풀었다.
그림 그리면서 해보니까 이해가 됐다. 
'''
import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline
n=int(input())
parent=[[0]*21 for i in range(n+1)] #노드마다 2**i만큼 떨어진 조상을 저장하는 배열
v=[0]*(n+1) #visited 함수 
d=[0]*(n+1) #각 노드의 depth 저장하는 배열 
g=[[] for i in range(n+1)] #그래프 저장하는 배열

for i in range(n-1): #그래프 저장 
  a,b=map(int,input().split())
  g[a].append(b)
  g[b].append(a)

def dfs(x,depth):
  v[x]=1 #x 방문 확인 
  d[x]=depth #depth가 x의 깊이
  for i in g[x]: #x에 이어진 노드들 차레로 확인 
    if v[i]: #i를 방문한 적이 없는 경우에만 진행 
      continue
    parent[i][0]=x #직계 부모 정보만 갱신, 나머지는 나중에 할 거 
    dfs(i,depth+1) #차례로 진행

def set_parent(): #모든 노드의 전체 부모 관계 갱신하는 함수
  dfs(1,0) #루트가 1번이라고 공지되어 있으므로 1부터 시작
  for i in range(1,21):
    for j in range(1,n+1):
      parent[j][i]=parent[parent[j][i-1]][i-1]
      #노드 j의 2**i번째 조상은 j의 2**(i-1)번째 조상의 2**(i-1)번째 조상이다.
      #ex) j의 8번째 조상은 j의 4번째 조상의 4번째 조상이다.
      #이거를 i가 1일 때부터 진행하면 전체가 다 채워진다.

def lca(a,b): #lca를 찾는 함수
  if d[a]>d[b]: #계산 편의를 위해 항상 b의 깊이가 더 크거나 같게 설정 
    a,b=b,a

  for i in range(21-1,-1,-1):
    if d[b]-d[a]>=2**i:
      b=parent[b][i]
  #a와 b의 깊이가 동일하도록 설정. LCA 1번과 다른 점은 시간 단축을 위해
  #이 과정에서도 sparse table 사용. 합성함수와 쿼리 문제에서 사용한 것과 동일
  if a==b: #a가 b의 조상이었던 경우 그냥 a가 정답 
    return a

  for i in range(21-1,-1,-1):
    if parent[a][i]!=parent[b][i]: #맨 끝부터 확인하다가 두 갈래가 되는 경우
      a=parent[a][i] #확인하는 노드를 갈라진 두 갈래의 노드로 바꿔줌 
      b=parent[b][i]
      '''계속 이해가 안 됐던 건 a,b를 바꿔준 뒤에도 같은 i를 사용한다는 점이었는데
        예를 들어 2**9만큼 떨어진 조상은 같은데 2**8만큼의 조상이 다르면
        a,b는 2**8 위치의 조상이 되고, i는 1 줄어 2**7부터 확인하게 된다.
        이때 새 a,b에서 2**8만큼 떨어진 조상이 바로 처음에 봤던 2**9 조상이므로
        공통임을 확인했기 때문에 볼 필요가 없다. 따라서 2**7부터 보면 전체 확인 가능하다.
        또한 i가 0일 때까지 확인하므로 마지막 a,b는 LCA를 부모로 가지는 노드이다.'''
  return parent[a][0] #마지막 a,b는 가장 LCA에 가까운 다른 값이므로 그 부모가 정답이다.

set_parent()
m=int(input())
for i in range(m):
  a,b=map(int,input().split())
  print(lca(a,b))
      
