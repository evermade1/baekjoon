'''
1753 최단경로 - 다익스트라 - Gold IV
다익스트라의 개념은 자료구조에서 공부했기 때문에 코드로 바꾸는 것만 공부했다.
다익스트라는 하나의 정점에서 다른 모든 정점까지의 최단경로를 구하는 알고리즘이다.
우선순위 큐가 필요하기 때문에 heapq를 사용한다. 큐에는 노드 - 시작 노드까지의 거리 쌍이 들어간다.
큐에 시작 노드 하나 넣고 시작한다. 원래 알던 거리보다 이번에 주어진 거리가 작거나 같을 때만 확인한다.
현재 노드에 연결된 노드들을 하나하나 확인하여, 원래 알던 거리보다 이번 거리+노드까지의 거리가
작은 경우에는 갱신해주고 큐에 넣는다.
큐가 최소 힙이기 때문에 weight가 작은 것부터 정렬된다. 
'''

import sys
graph=[]
input=sys.stdin.readline
inf=sys.maxsize
v,e=map(int,input().split())
s=int(input())
for i in range(v+1):
    graph.append([])
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((c,b)) #(weight, 도착점) 형태로 저장 
import heapq  # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
  d = [float('inf') for i in range(v+1)]  # start로 부터의 거리 값을 저장하는 배열, 전부 무한대로 초기화  
  d[start] = 0  # 시작점까지의 거리는 0
  queue = [] # 탐색을 위한 큐, 앞으로 탐색하고자 하는 노드를 push 
  heapq.heappush(queue, [d[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    current_c, current_b = heapq.heappop(queue)  # 탐색 할 노드, 거리를 queue에서 가져옴.

    if d[current_b] < current_c:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음 - 값이 작아질 수 없기 때문 
      continue
    
    for i in graph[current_b]: #딕셔너리에서 item 사용하면 key, value 동시에 받을 수 있음
      new_b,new_c=i[1],i[0]
        #이번에 탐색하는 노드에 연결되어 있는 노드들을 하나하나 탐색
      distance = current_c + new_c  # 이번 노드까지의 weight에 연결된 노드까지의 weight 더함 - 경유한 경우의 거리 
      if distance < d[new_b]:  # 이전에 들어있던 거리 보다 작으면 갱신
        d[new_b] = distance
        heapq.heappush(queue, [distance, new_b])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        #갱신되었기 때문에 큐에 넣어서 다시 확인 
  return d

ans=dijkstra(graph,s)
c=0
for k in ans:
    if not c:
        c+=1
        continue
    if k==float('inf'):
        print('INF')
    else:
        print(k)
    
