'''
2042 구간 합 구하기 - 세그먼트 트리 
세그먼트 트리 - 특정 데이터 구간의 정보를 가장 빠르게 구할 수 있는 방법
구간 합으로 예시를 들면 우선 루트에 전체 데이터의 합을 저장하고,
left에 왼쪽 반, right에 오른쪽 반 데이터의 합을 저장하는 식으로 반복한다.
이 때 루트의 인덱스를 기존 트리는 0으로 하지만 여기서는 1로 하는데,
이렇게 하면 루트 x의 left의 인덱스가 항상 x*2가 되기 때문이다.
데이터가 홀수 개일때를 감안하여 나머지를 버린 값을 기준으로 분리한다.
트리의 원소 개수는 데이터 개수보다 큰 최소의 제곱수 *2이다.
트리 구조이기 때문에 O(logN)으로 해결할 수 있다.
'''
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))
l=[0]*(n*4) #4를 곱하면 최소 제곱수*2까지 커버 가능 
def init(s,e,n): #구간 합 트리를 만드는 함수 
  if s==e:
    l[n]=a[s]
    return l[n]
  m=(s+e)//2
  l[n]=init(s,m,n*2)+init(m+1,e,n*2+1)
  return l[n]

def f(s,e,n,left,right): #구간 합을 구하는 함수
  #s,e: 전체 크기에서의 범위
  #left,right: 구하고 싶은 범위 
  if left>e or right<s: return 0 #원하는 구간 전체가 범위 밖인 경우
  #ex)s<e<left<right
  if s>=left and e<=right: return l[n] #구간 전체가 범위 안인 경우
  #left<s<e<right
  m=(s+e)//2
  return f(s,m,n*2,left,right)+f(m+1,e,n*2+1,left,right) #일부는 밖 일부는 안인 경우 

def update(s,e,n,i,dif): #인덱스 값을 변경하는 함수
  if i<s or i>e: return #범위 밖에 있는 경우
  l[n]+=dif #차이만큼 바꿔주기
  if s==e: return #가장 작은 인덱스인 경우 리턴 (leaf인 경우)
  m=(s+e)//2
  update(s,m,n*2,i,dif)
  update(m+1,e,n*2+1,i,dif)

init(0,n-1,1)
for i in range(m+k):
  A,b,c=map(int,input().split())
  if A==1:
    update(1,n,1,b,c-a[b-1])
    a[b-1]=c
  else:
    print(f(1,n,1,b,c))
