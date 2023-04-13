'''
12015 가장 긴 증가하는 부분 수열 2 - 이분 탐색 
정답을 저장하는 배열을 하나 [0] 으로 초기화한다. d라고 하자.
앞에서부터 하나씩 확인한다. d[-1]보다 크면 d에 추가한다.
크지 않으면 이분 탐색으로 넣을 위치를 찾아 기존 값과 바꾼다.
여기서 넣을 위치란 지금 값보다 큰 값 중 가장 작은 값의 위치이다.
이 방법의 문제는 d가 실제 LIS와는 다르고, 길이만 같다는 것이다.
따라서 LIS를 요구하는 문제에서는 다른 풀이가 필요하다.
bisect 모듈을 사용해서도 풀 수 있다.
밑의 else 부분을 else: d[bisect_left(d,i)]=i 하면 d에서 i의 위치를 알 수 있다. 
'''
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
d=[0]
for i in l:
  if d[-1]<i:
    d.append(i)
  else:
    s=0
    e=len(d)
    while s<e:
      m=(s+e)//2
      if d[m]<i:
        s=m+1
      else:
        e=m
    d[e]=i
print(len(d)-1)
