'''
2110 공유기 설치 - 이분 탐색 - Gold IV
이분 탐색으로 푸는 문제라는 것만 인식하면 쉽게 풀 수 있다.
start(s) : 1 (가능한 가장 작은 값)
end(e) : 집의 좌표를 고려하지 않고 범위만 생각했을 때 가능한 가장 큰 값
            (집이 있는 범위)//(공유기 수 - 1)
이를 가지고 이분 탐색을 진행한다.
첫 집에는 무조건 공유기를 설치한다.
이후 공유기를 설치한 집과 m 이상 떨어진 집마다 다시 공유기를 설치한다.
이렇게 해서 설치한 공유기의 개수가 입력값 이상이면 s=m+1,
아니면 e=m-1로 바꾼 뒤 반복한다.
'''
import sys
n,c=map(int,input().split())
l=[]
for i in range(n):
  l.append(int(input()))
l.sort()
s,e=1,(l[-1]-l[0]+1)//(c-1)
while s<=e:
  m=(s+e)//2
  print(s,e,m)
  tmp=l[0]
  k=1
  for i in range(1,n):
    if l[i]>=tmp+m:
      k+=1
      tmp=l[i]
  print(k)
  if k>=c:
    s=m+1
  else:
    e=m-1
print(s-1)
