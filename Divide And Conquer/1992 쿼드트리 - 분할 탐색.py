'''
1992 쿼드트리 - 분할 탐색 - Silver I
2의 n승 크기의 변을 가지는 정사각형 배열을 받아 정리하는 문제이다.
주의할 점은 인풋이 띄어쓰기 없이 주어지므로 두 번에 나누어 정리해야 한다.
f(x,y,z) 함수는 분할 탐색을 위한 함수이다.
x와 y는 이번 함수에서의 탐색 기준점이 l[x][y]으로 하도록 한다.
z는 해당 위치에서부터 z만큼 떨어진 곳까지를 탐색하도록 한다.
이렇게 해당 구역을 탐색하는데, 전부 0 또는 1인지를 확인하기 위해 합을 사용한다.
해당 구역의 총합이 0이면 전부 0, 총합이 해당 구역의 넓이와 같으면 전부 1이다.
출력은 ans 배열에 먼저 넣어놓고 나중에 진행한다.
해당 구역이 전부 0 또는 1이면 ans에 0 또는 1을 append한다.
아닌 경우 우선 '('를 append하고, 구역을 네 개로 나누어 f를 재귀한다.
네 개의 함수 이후 ')'를 append하여 괄호를 닫는다.
이렇게 만든 ans를 문제 조건에 맞게 출력한다.
'''
import sys
n=int(input())
l=[]
for i in range(n):
    k=input()
    p=[]
    for i in k:
        p.append(int(i))
    l.append(p)

ans=[]
def f(x,y,z):
    if z==1:
        ans.append(l[x][y])
        return
    c=0
    for i in range(z):
        for j in range(z):
            c+=l[x+i][y+j]
    if c==0:
        ans.append(0)
    elif c==z**2:
        ans.append(1)
    else:
        ans.append('(')
        f(x,y,z//2)
        f(x,y+z//2,z//2)
        f(x+z//2,y,z//2)
        f(x+z//2,y+z//2,z//2)
        ans.append(')')
f(0,0,n)
print(*ans,sep='')
