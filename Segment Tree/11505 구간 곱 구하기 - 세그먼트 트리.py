'''
11505 구간 곱 구하기 - 세그먼트 트리
구간 합 구하기 문제를 조금 변형하면 풀 수 있는 문제이다.
처음엔 그냥 더하기만 곱하기로 다 바꿔서 냈는데 당연히 틀렸다.
우선 범위를 벗어난 경우 return 0이 아닌 1로 해야 곱한 값이 보존된다.
또한 update에 0이 있을 경우 제대로 된 연산이 안 되기 때문에 조금 바꿔야 하는데,
기존에 그냥 노드 값들에 직접 연산을 진행했다면,
이번엔 리프 노드 값을 바꿔준 뒤에 하나하나 곱하는 식으로 바꿔야 했다.
그러지 않으면 기존 값이 0인 경우 0으로 나누어야 하는 경우가 발생하기 때문이다.
'''
import sys
input=sys.stdin.readline
n,m,k=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))
l=[1]*(n*4) #4를 곱하면 최소 제곱수*2까지 커버 가능 
def init(s,e,n): #구간 곱 트리를 만드는 함수 
  if s==e:
    l[n]=a[s]
    return l[n]
  m=(s+e)//2
  l[n]=(init(s,m,n*2)*init(m+1,e,n*2+1))%1000000007
  return l[n]

def f(s,e,n,left,right): #구간 합을 구하는 함수
  #s,e: 전체 크기에서의 범위
  #left,right: 구하고 싶은 범위 
  if left>e or right<s: return 1 #원하는 구간 전체가 범위 밖인 경우
  #ex)s<e<left<right
  if s>=left and e<=right: return l[n] #구간 전체가 범위 안인 경우
  #left<s<e<right
  m=(s+e)//2
  return (f(s,m,n*2,left,right)*f(m+1,e,n*2+1,left,right))%1000000007 #일부는 밖 일부는 안인 경우 

def update(s,e,n,i,x): #인덱스 값을 변경하는 함수
  if i<s or i>e: return #범위 밖에 있는 경우
  if s==e:
    l[n]=x
  else:
    m=(s+e)//2
    update(s,m,n*2,i,x)
    update(m+1,e,n*2+1,i,x)
    l[n]=l[n*2]*l[n*2+1]%1000000007

init(0,n-1,1)
for i in range(m+k):
  A,b,c=map(int,input().split())
  if A==1:
    update(1,n,1,b,c)
    a[b-1]=c
  else:
    print(int(f(1,n,1,b,c)%1000000007))
