'''
16565 N포커 - 포함 배제의 원리
dp로 풀라는데 그냥 풀었더니 파이썬 전체 시간 1위했다.
포함 배제의 원리는 합집합을 뺐다 더했다 하는 건데,
설명하기 어려우므로 그냥 까먹었으면 찾아보자.
카드 n개를 뽑으면 포카드가 되는 경우의 수를 출력하는 문제인데,
n개로 만들 수 있는 포카드의 개수는 1개에서부터 n//4개까지이므로
1개일때 경우의 수 - 2개일 때 경우의 수 + 3개일 때 경우의 수 이런 식으로 만들었다.
'''
import sys
import math
input=sys.stdin.readline

def f(x,y):
    return math.factorial(x)//(math.factorial(y)*math.factorial(x-y))
ans=0
n=int(input())
for i in range(1,n//4+1):
    import sys
import math
input=sys.stdin.readline

def f(x,y):
    return math.factorial(x)//(math.factorial(y)*math.factorial(x-y))
ans=0
n=int(input())
for i in range(1,n//4+1):
    k=(-1)**(i-1)*f(13,i)*f(52-(4*i),n-(4*i))
    #print(i,k)
    ans+=k
    ans%=10007
print(ans)
