'''
2357 최솟값과 최댓값 - 세그먼트 트리
먼저 푼 세그먼트 트리 문제들과 거의 동일한 코드를 사용한다.
합이나 곱을 만드는 식만 최댓값, 최솟값으로 바꿔주면 된다.
배열도 이차원으로 만들어 최대 최소를 동시에 저장하도록 한다.
'''
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
a=[]
for i in range(n):
  a.append(int(input()))
l=[[0,1e9] for i in range(n*4)]
def fmax(s,e,n):
  if s==e:
    l[n][0]=a[s]
    return l[n][0]
  m=(s+e)//2
  l[n][0]=max(fmax(s,m,n*2),fmax(m+1,e,n*2+1))
  return l[n][0]

def fmin(s,e,n):
  if s==e:
    l[n][1]=a[s]
    return l[n][1]
  m=(s+e)//2
  l[n][1]=min(fmin(s,m,n*2),fmin(m+1,e,n*2+1))
  return l[n][1]

def f1(s,e,left,right,n):
  if s>=left and e<=right:
    return l[n][0]
  if s>right or e<left:
    return 1
  m=(s+e)//2
  return max(f1(s,m,left,right,n*2),f1(m+1,e,left,right,n*2+1))

def f2(s,e,left,right,n):
  if s>=left and e<=right:
    return l[n][1]
  if s>right or e<left:
    return 1e9
  m=(s+e)//2
  return min(f2(s,m,left,right,n*2),f2(m+1,e,left,right,n*2+1))

fmax(0,n-1,1)
fmin(0,n-1,1)
for i in range(m):
  x,y=map(int,input().split())
  if x>y:
    x,y=y,x
  print(f2(1,n,x,y,1),f1(1,n,x,y,1))
