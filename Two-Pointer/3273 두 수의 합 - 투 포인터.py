'''
3273 두 수의 합 - 투 포인터 - Silver III
두 수를 합해 x가 되는 쌍의 개수를 찾는 문제이다.
투 포인터는 이분 탐색과 코드가 비슷하지만,이분 탐색은 m을 사용함과 달리
투 포인터에서는 m을 사용하지 않고 1씩 가까워지는 형식이다.
start(s) : 첫 원소의 위치 (0)
end(n) : 마지막 원소의 위치 (n-1)
s와 n 위치에 있는 원소의 합이 x보다 크면 n을 1 내려 합을 감소시킨다.
x보다 작으면 s를 1 올려 값을 증가시킨다.
x이면 카운트를 1 올리고 s와 n을 모두 변화시킨다.
x이면 s와 n 중 하나만 변화시킬 경우 값이 x가 될 수 없기 때문이다.
'''
n=int(input())
l=list(map(int,input().split()))
x=int(input())
l.sort()
n-=1
s=0
ans=0
while l[n]>x:
  n-=1
while s<n:
  if l[s]+l[n]>x:
    n-=1
  elif l[s]+l[n]<x:
    s+=1
  else:
    ans+=1
    n-=1
    s+=1
print(ans)
