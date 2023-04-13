'''
1068 트리 - 트리
리프 노드의 개수를 구하는 문제다. 다만 노드 하나를 제거하여 그 밑까진 다 없앤다.
여러 방법이 있겠지만 좀 잡기술스러운 방법으로 풀었다.
일단 dfs에 용이한 방식으로 트리를 저장해 준 뒤
지워져야 하는 노드는 자식 노드를 저장하는 배열을 [1]로 만들어 준다.
그러면 자식 노드 배열이 []인 노드가 리프 노드이므로 이 개수만 구하면 된다.
단 여기서 지운 노드를 자식으로 가지는 노드가 자식이 걔 하나였다면
걔를 지우면 리프 노드가 된다는 점까지 확인해 주어야 한다.
이 과정은 한 번 존재하기 때문에 그냥 remove를 통해 지워주었다. 
'''
import sys
input=sys.stdin.readline
n=int(input())
d=[[] for i in range(n)]
l=list(map(int,input().split()))
def f(x):
    for i in d[x]:
        f(i)
    d[x]=[1]
for i in range(n):
    if l[i]!=-1:
        d[l[i]].append(i)
x=int(input())
if x in d[l[x]]:
    d[l[x]].remove(x)
f(x)
ans=0
for i in d:
    if not i:
        ans+=1
print(ans)
