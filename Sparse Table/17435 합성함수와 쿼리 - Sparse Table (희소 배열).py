'''
17435 합성함수와 쿼리 - Sparce Table 희소 배열
Sparce Table이란 배열 원소의 개수가 배열의 길이보다 적은 배열을 의미한다.
f-f 형식의 합성함수를 계산하기에 좋은 알고리즘이다.
합성함수 연산을 n번 처리하는 것보단 미리 2^k번째의 값을 저장해 놓고
꺼내서 사용하면 분할 탐색과 같이 시간을 로그 스케일로 줄일 수 있다.
우선 식을 보기 편하게 하기 위해 0번째 원소는 전부 0으로 처리하였다.
l은 문제에서 주어진 연산 횟수의 최댓값인 500000보다 작은 최대의 2의 제곱이 2^19이므로
19번째까지 배열을 만들었다. l[i]는 2*i번 연산했을 때의 값이다.
이제 n이 주어지면 2^j보다 n이 클 경우 빼면서 배열에서 2^j번 연산한 값을 찾아서
x를 바꿔준다. 이를 2^0까지 반복하면 처음 n만큼 연산했을 때의 결과가 나오게 된다.
이게 배열의 0번째 원소, 2*0이 1인 점 이런 것 때문에 조금씩 헷갈려서 좀 걸렸다.
'''
import sys
input=sys.stdin.readline
n=int(input())
k=[0]+list(map(int,input().split()))
l=[k]+[[0 for i in range(n+1)] for j in range(19)]
for i in range(1,20):
  for j in range(1,n+1):
    l[i][j]=l[i-1][l[i-1][j]]
def f(n,x):
  a=x
  for j in range(18,-1,-1):
    if n>=2**j:
      n-=2**j
      a=l[j][a]
  return a
    
for i in range(int(input())):
  n,x=map(int,input().split())
  print(f(n,x))
