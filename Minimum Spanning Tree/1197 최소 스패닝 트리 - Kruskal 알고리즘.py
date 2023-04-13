'''
1197 최소 스패닝 트리 - 최소 스패닝 트리 (MST) - Kruskal 알고리즘
1. 그래프의 간선들을 가중치가 낮은 순서로 정렬
2. 가장 낮은 간선부터 차례로 선택
3. 사이클이 발생하는 간선은 선택x (유니온 파인드로 확인)
'''
v,e=map(int,input().split())
l=[]
for i in range(e):
    a,b,c=map(int,input().split())
    l.append([a,b,c])
l.sort(key=lambda x:x[2])

parent=[i for i in range(v+1)]
#find 구현
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x]) #찾는 구간에 있는 노드들의 부모를 전부 루트 노드로 바꿔주기
    return parent[x]
#루트 노드를 찾으면서 트리의 구조르 루트 노드에 전부 붙어있는 형태로 바꿔
#트리의 효율을 올리기 


ans=0
for i in l:
    if find(i[0])!=find(i[1]):
        parent[find(i[0])]=find(i[1])
        ans+=i[2]
print(ans)
