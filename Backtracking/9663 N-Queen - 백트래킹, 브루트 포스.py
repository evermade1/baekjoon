'''9663 N-Queen - 백트래킹, 브루트 포스 - Gold IV
이차원 배열로 퀸이 놓인 좌표를 저장하는 것이 아니라,
대신 0으로 초기화된 일차원 배열 만들어놓고 사용하기
세로줄마다 가능한 모든 자리에 퀸 놓고 다음 세로줄로 넘어가,
전체 경우의 수를 계산하는 방식
g(x)는 퀸이 놓여도 되는 자리인지 판별하는 함수.
i==x : 지금까지 사용된 자리인지 판별
l[i]==l[x] : 지금까지의 퀸이 직선으로 잡을 수 있는 자리인지 판별
abs(i-x)==abs(l[i]-l[x]) : 지금까지의 퀸이 대각선으로 잡을 수 있는 자리인지 판별
f(x)는 경우의 수를 계산하는 메인 함수
현재의 세로줄 x에서 일단 모든 경우의 수를 만들어 보내고,
g(x)를 통해 판별하여 놓아도 되는 자리라면 다음 세로줄로 이동
끝까지 이동했다면 경우의 수 1 추가 
'''
n=int(input())
s=[]
ans=0
l=[0 for i in range(n)]
def g(x):
    for i in range(x):
        if i==x or l[i]==l[x] or abs(i-x)==abs(l[i]-l[x]):
            return False
    return True
def f(x):
    global ans
    if x==n:
        ans+=1
        return
    else:
        for i in range(n):
            l[x]=i
            if g(x):
                f(x+1)
f(0)
print(ans)
