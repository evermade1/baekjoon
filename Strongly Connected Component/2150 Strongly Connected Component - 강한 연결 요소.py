'''
2150 Strongly Connected Component - 강한 연결 요소 
강한 연결 요소 - 그래프 안에서 강하게 연결된 정점의 집합, SCC라고 부름
특징 : 같은 SCC에 속하는 두 정점은 서로 도달이 가능하다.
사이클이 발생하면 무조건 SCC, 방향성 그래프에서만 의미가 있다.
Kosaraju's Algorithm : 구현 쉬움
Tarjan's Algorithm : 적용이 쉬움 - 일단 이거부터
타잔 - 모든 정점에 대해 dfs - SCC 찾는 알고리즘
  자신의 부모와 연결이 되어 있으면 그 경로에 한해서 SCC가 성립한다.
  dfs 하면서 만나는 노드 스택에 넣음, 처음 들어간 정점인 경우 자신을 부모로 함
  dfs 돌다가 아직 dfs가 끝나지 않은 정점 발견한 경우
  걔 부모랑 내 부모 비교 - 더 작은 거로 갱신하고 dfs 종료 
  dfs 끝난 시점에서 (더 이상 방문할 노드가 없을 때)
  현재 노드의 부모가 해당 노드 자신인 경우 자신이 부모임을 깨닫고
  스택에서 자기 자신이 나올 때까지 모두 뽑음 - SCC 그룹 하나 발견
  다만 여기서 비교하는 부모 값이라는 건 노드 번호가 아닌 고유 id이다.
  이 id는 탐색하는 순서대로 부여해 주어야 한다.
'''
import sys
import collections
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
v,e=map(int,input().split())
g=[[] for i in range(v+1)]

for _ in range(e):
  a,b=map(int,input().split())
  g[a].append(b)

d=[-1 for i in range(v+1)] #방문 배열 
stack=[]
on_stack=[False for i in range(v+1)] #스택 안에 있는지 확인하는 배열 
id=0 #탐색 순서대로 값 주기 위한 아이디 
ans=[]

def dfs(x):
  global id
  id+=1
  d[x]=id #방문 표시 
  stack.append(x) # 스택에 넣기 
  on_stack[x]=True #스택에 있음을 표시 
  parent=d[x] #부모를 id로 해 놓음  
  for i in g[x]: #연결된 노드들에 대해 
    if d[i]==-1: #방문하지 않은 노드인 경우 
      parent=min(parent,dfs(i)) #x와 i 중 작은 부모의 값으로 x의 부모 설정
                                             #이 때 i의 부모값은 다음 dfs에서 정해짐 (재귀)
    elif on_stack[i]==True: #방문했지만 dfs가 끝나지 않은 노드인 경우 
      parent=min(parent,d[i]) #마찬가지, 다만 d[i]가 존재하므로 d[i] 사용
  if parent==d[x]: #자신이 자신의 부모인 경우
    #처음에 d[x]로 해놨기 때문에 다 걸릴 것 같지만 아님
    #재귀하다 보면 1개짜리 SCC가 아닌 이상 안 걸림 
    scc=[]
    while True: #스택에서 자신 나올 때까지 꺼내기 
      node=stack.pop()
      on_stack[node]=False
      scc.append(node)
      if x==node:
        break
    scc.sort() #문제 요구조건 
    scc.append(-1) #문제 요구조건 
    ans.append(scc)
  return parent

for i in range(1,v+1):
  if d[i]==-1:
    dfs(i)
ans.sort()
print(len(ans))
for i in ans:
  print(*i)
