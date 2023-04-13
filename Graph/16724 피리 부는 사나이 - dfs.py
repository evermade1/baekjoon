'''
16724 피리 부는 사나이 - dfs
dfs로 창의적으로 풀어서 뿌듯했는데 찾아보니까 유니온 파인드로도 풀 수 있더라
근데 dfs로 푼 게 아까워서 남긴다.
최소 사이클의 개수로 맵 전체를 다 채워야 하는데,
아무 위치나 잡아서 시작해도 최소를 구할 수 있게 하기 위해
사이클마다 숫자를 잡아서 (p) d를 해당 숫자로 채워가며 이동하도록 했다.
이렇게 해서 진행하다 지금 쓰고 있는 p를 만났다면 사이클이 완성된 것이고,
0이 아닌 다른 숫자를 만났다면 다른 사이클에 지금까지의 경로를 합칠 수 있다는 의미이다.
이렇게 만난 경우 합치면서 0이 없을 때까지 진행하면 최소 사이클 개수를 알 수 있다.
'''
n,m=map(int,input().split())
d=[[0 for i in range(m)] for j in range(n)]
l=[]
for i in range(n):
  l.append(list(input()))
ans=[0]
def dfs(x,y,t):
  d[x][y]=t
  k=l[x][y]
  c=0
  if k=='U':
    if x-1>=0:
      if d[x-1][y]==0:
        c+=1
        dfs(x-1,y,t)
      elif d[x-1][y]!=t:
        c=-1
  elif k=='D':
    if x+1<n:
      if d[x+1][y]==0:
        c+=1
        dfs(x+1,y,t)
      elif d[x+1][y]!=t:
        c=-1
  elif k=='L':
    if y-1>=0:
      if d[x][y-1]==0:
        c+=1
        dfs(x,y-1,t)
      elif d[x][y-1]!=t:
        c=-1
  elif k=='R':
    if y+1<m:
      if d[x][y+1]==0:
        c+=1
        dfs(x,y+1,t)
      elif d[x][y+1]!=t:
        c=-1
  if c==0:
    '''for i in d:
      print(*i)
    print()'''
    ans[0]+=1
  #d[x][y]=0

p=0
for i in range(n):
  for j in range(m):
    if d[i][j]==0:
      p+=1
      dfs(i,j,p)
print(ans[0])
