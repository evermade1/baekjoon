'''
1202 보석 도둑 - 최소 힙, 최대 힙
보석과 가방 모두 무게/용량이 작은 순서로 정렬하고
가방마다 항상 들어갈 수 있는 보석 중 가장 가치가 높은 보석을 넣으면 된다.
heapq에 보석의 무게와 가치를 넣는다.
가방마다 용량 내의 보석을 새로운 heapq t에 넣는다.
이때 최대 힙을 구현하기 위해 가치에 음수를 붙여서 넣어준다.
다 끝나면 t 맨 앞의 값이 가장 가치가 큰 값이므로 음수를 떼서 ans에 더한다.
다음 가방에는 이전 가방에 들어가는 보석은 t에 다 들어있기 때문에
이전 가방에는 안 들어가고 이번 가방에는 들어가는 애들만 t에 넣어준다.
이 과정에서 시간이 절약된다.
마찬가지로 현재 t에서 가장 가치가 큰 보석을 넣어준다.
최대/최소 힙을 아직 자유롭게 쓰지 못해서 답을 보고 풀었다.
우선순위 큐라는 게 그냥 최대/최소 힙이라고 생각하고 풀면 좋을 것 같다. 
'''
import sys
import heapq
input=sys.stdin.readline
n,k=map(int,input().split())
l=[]
d=[]
for i in range(n):
    heapq.heappush(l,list(map(int,input().split())))
for i in range(k):
    d.append(int(input()))
d.sort()
t=[]
ans=0
for i in d:
    while l and i>=l[0][0]:
        heapq.heappush(t,-(heapq.heappop(l))[1])
    if t:
        ans-=heapq.heappop(t)
print(ans)
