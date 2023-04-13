'''
1655 가운데를 말해요 - 우선순위 큐 - Gold II
heapq로 최대, 최소 힙을 만들어서 사용하는 문제이다.
최대나 최소를 뽑는 게 아닌 중간값을 뽑아야 하므로, 최대 힙과 최소 힙을
다 사용하여, 최대 힙에 최소~중간값, 최소 힙에 중간 다음 값~최댓값이 들어가게 한다.
heapq는 기본적으로 최소 힙 형태이기 때문에,
최대 힙으로 사용하려면 (-1*k,k)의 형태로 넣어 음수 기준이 되도록 해야 한다.
최대 힙에 값을 먼저 넣고, 최대 힙의 크기가 더 커지면 최소 힙에 값을 넣는다.
이후 두 힙의 최우선 값을 비교하여 순서를 맞춘다.
두 값은 최소 힙의 최솟값과 최대 힙의 최댓값이기 때문에 이 둘의 순서만 맟추면 
이렇게 하면 항상 최대 힙의 최우선 값이 중간값이 된다.
우선순위 큐를 리스트 형식으로 봤을 때 정렬되어 있지 않기 때문에 (트리 형태)
이런 식으로 만들어 줘야 한다.
'''
import sys
import heapq
q1=[]
q2=[]
ans=[]
for i in range(int(sys.stdin.readline())):
  k=int(sys.stdin.readline())
  if len(q1)==len(q2):
    heapq.heappush(q1,(-1*k,k))
  else:
    heapq.heappush(q2,k)
  if q2 and q1[0][1]>q2[0]:
    a,b=heapq.heappop(q1)[1],heapq.heappop(q2)
    heapq.heappush(q1,(-1*b,b))
    heapq.heappush(q2,a)
  print(q1[0][1])
