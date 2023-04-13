'''
2887 행성 터널 - 최소 스패닝 트리
처음으로 푼 플래티넘 문제라 남긴다.
처음에 메모리 초과가 계속 떠서 그냥 찾아봤는데 좋은 방법이 있었다.
원래 방법대로는 n개의 노드를 하나하나 연결하는 간선을 모두 append했으므로
n(n+1)/2개의 간선이 저장되었는데,
이 문제에서는 행성 간 거리를 x,y,z 좌표간 거리 중 최솟값으로 사용하기 때문에
x,y,z마다 배열을 만들어 정렬해 준 뒤 배열 내에서 인접해 있는 행성 간의 간선만
저장하면 된다. 이 때 저장되는 간선의 개수는 3*(n-1)개로 많이 줄어든다.
이 방법을 사용하면 x,y,z 각각의 배열에서 저장하면서 중복되는 간선이 생길 수 있는데,
어차피 ans라는 하나의 배열에 다시 모아서 정렬한 뒤 진행하는 과정에서
중복된 간선은 사이클로 인식되어 사용되지 않는다.
ans는 x,y,z 배열에서의 가까운 거리를 가진 간선들을 다시 정렬하였기 때문에
이 배열에서 n-1번째까지만 조사하면 (사이클 제외) 정답을 얻을 수 있다.
처음에 시도한 방법도 맞는 방법이지만 메모리 및 시간 초과를 방지하기 위한 방법이다.
'''
import sys
input=sys.stdin.readline
n=int(input())
lx,ly,lz=[],[],[]
for i in range(n):
    x,y,z=map(int,input().split())
    lx.append([x,i])
    ly.append([y,i])
    lz.append([z,i])
lx.sort()
ly.sort()
lz.sort()
k=[]

ans=[]
for i in lx,ly,lz:
    for j in range(1,n):
        ans.append([i[j-1][1],i[j][1],i[j][0]-i[j-1][0]])
parent=[i for i in range(n)]
#find 구현
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x]) #찾는 구간에 있는 노드들의 부모를 전부 루트 노드로 바꿔주기
    return parent[x]
#루트 노드를 찾으면서 트리의 구조르 루트 노드에 전부 붙어있는 형태로 바꿔
#트리의 효율을 올리기 


ans.sort(key=lambda x:x[2])
answ=0
x=0
for i in ans:
    if x==n:
        break
    if find(i[0])!=find(i[1]):
        x+=1
        parent[find(i[0])]=find(i[1])
        answ+=i[2]
print(answ)
