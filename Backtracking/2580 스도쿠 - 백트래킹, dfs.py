'''2580 스도쿠 - 백트래킹, dfs - Gold IV
우선 스도쿠 내의 빈 칸을 리스트 k에 넣는다.
g(x)는 현 좌표가 스도쿠 내 9개의 정사각형 중 어디에 있는지 찾을 때 필요한 함수로,
x 또는 y좌표에 따라 구간을 세 개로 나눠 리턴한다.
f(x,y,c)는 좌표 (x,y)에 값 c가 들어갈 수 있는지 판별하는 함수이다.
g(x) 함수로 정사각형 내에 c가 있는지 판별하고, 세로/가로줄 또한 판별한다.
dfs 함수는 k에 대해 dfs를 진행하는 함수이다.
만약 모든 k가 채워졌다면 정답이므로 해당 값을 출력하고 리턴한다.
다른 dfs가 계속해서 실행되고 있으므로 exit(0)를 이용해 탈출한다.
아닌 경우 1부터 10까지 넣어보고 가능하다면 다음 빈 칸으로 이동한다.
이번 dfs를 위해 채운 값은 다음 dfs를 위해 다시 비운다.
'''
l=[]
for i in range(9):
    k=list(map(int,input().split()))
    l.append(k)
k=[]
for i in range(9):
    for j in range(9):
        if l[i][j]==0:
            k.append([i,j])
def g(x):
    if 2>=x>=0:
        return [0,1,2]
    elif 5>=x>=3:
        return [3,4,5]
    else:
        return [6,7,8]
def f(x,y,c):
    a=g(x)
    b=g(y)
    for i in range(9):
        if l[x][i]==c:
            return False
    for i in range(9):
        if l[i][y]==c:
            return False
    for i in a:
        for j in b:
            if l[i][j]==c:
                return False
    return True
def dfs(n):
    if n==len(k):
        for i in range(9):
            print(*l[i])
        exit(0)
    for i in range(1,10):
        x=k[n][0]
        y=k[n][1]
        if f(x,y,i):
            l[x][y]=i
            dfs(n+1)
            l[x][y]=0 #다음 dfs를 위해 다시 원래대로 돌려놓기
dfs(0)
