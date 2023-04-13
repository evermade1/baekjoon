'''
11404 플로이드 - 플로이드-와샬 알고리즘 - Gold IV
다익스트라로도 가능하지만 문제의 조건과 상황에 따라
플로이드 - 와샬 알고리즘이 더 빠른 경우가 있다.
플로이드 - 와샬 알고리즘은 2차원 배열을 하나하나 탐색하는 동안
삼중 for문을 사용하여 j에서 k까지 가는 동안 경유할 수 있는 모든 i를 경유하는 경우를 모두 계산하여
어디를 경유해야 가장 빠른지를 찾는 알고리즘이다.
삼중 for문 때문에 O(n^3)이다.
경유지가 맨 앞 for문에서 나와야 한다는게 특징이다. 이렇지 않으면 누락이 발생한다. 
전체 경우의 수를 모두 확인할 수 있다.
예를 들어 1에서 4로 가는 최단거리가 1 5 3 4 순서라고 가정하자.
이는 1에서 3 가는 최단도 1 5 3, 5에서 4 가는 최단도 5 3 4 라는 의미를 내포한다.
1에서 4 가는 최단거리가 결정되는 순간은 k=5 일 때인데,
k=3일 때 5 3 4가 결정되고, k=5일 때 1 5 4가 결정되기 때문이다.
'''

import sys
from sys import stdin
inf=int(1e9)
n=int(stdin.readline())
m=int(stdin.readline())
g=[[float('inf') for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    a,b,c=map(int,stdin.readline().split())
    g[a][b]=min(g[a][b],c)
for i in range(n+1):
    g[i][i]=0
for i in range(1,n+1): #경유지
    for j in range(1,n+1): #출발지
        for k in range(1,n+1): #도착지
            g[j][k]=min(g[j][k],g[j][i]+g[i][k])

for i in range(1,n+1):
    for j in range(1,n+1):
        if g[i][j]==float('inf'):
            print(0,end=' ')
        else:
            print(g[i][j],end=' ')
    print()
