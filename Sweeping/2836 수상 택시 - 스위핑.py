'''
2836 수상 택시 - 스위핑
2170 선 긋기의 개념을 가지고 오면 금방 풀 수 있는 문제다.
사실 스위핑이 뭔지 모르고 쓰고 있는데 정렬만 잘 해놓고 생각 잘 하면 풀 수 있는 문제다.
상근이가 0에서 m까지 가는 동안 다른 사람들을 태워줄 때 거리의 최소를 구하는 문젠데,
양의 방향으로 가는 사람들은 고려할 필요가 없다는 점만 알면 쉽다.
이 사람들은 어차피 상근이가 m으로 이동하는 동안 이동할 수 있기 때문이다.
따라서 음의 방향으로 가는 사람들만 l에 append해준 뒤, 2170에서처럼
중복을 제외한 이동 변위의 크기를 만들어 준다. 이를 x라고 하겠다.
예제에서 상근이의 이동 경로를 그려보면, 0에서 m까지 이동하는 동안
x만큼은 돌아갔다가 다시 오므로 2*x만큼을 원래 경로에 더해주면 된다는 사실을 알 수 있다.
'''
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
l=[]
for i in range(n):
    k=list(map(int,input().split()))
    if k[0]>k[1]:
        l.append([k[1],k[0]])
l.sort(key=lambda x:x[1]-x[0])
l.sort(key=lambda x:x[1])
l.reverse()
ans=l[0][1]-l[0][0]
a,b=l[0]
for i in range(1,len(l)):
    if b>=l[i][1] and a<=l[i][0]: #전꺼에 포함될 때
        continue
    if a>=l[i][1]: #전꺼랑 떨어져 있을 때 
        ans+=l[i][1]-l[i][0]
    else: #전꺼랑 부분적으로 겹쳐있을 때 
        ans+=a-l[i][0]
    a,b=l[i]
print(m+2*ans)
