'''
15824 너 봄에는 캡사이신이 맛있단다 - 분할 정복
할 만 했는데 답을 봐 버렸다. 두 가지를 찾지 못했다.
우선 각 원소가 최대 또는 최소가 되는 횟수만 찾으면 되는데
그걸 묶어서 계산하려고 했던 점이 패착이었다.
일단 정렬을 해 놓으면 i번째 원소가 최댓값이 되는 경우는
2**i번, 최솟값이 되는 경우는 2**(n-i-1)번이다. 이는 앞뒤 원소 개수마다
on/off의 두 가지 경우의 수가 발생하며, 전부 off인 경우를 빼면 나온다.
여기까지 하면 50점이고, 파워 함수를 분할 정복으로 직접 만들어야 정답이다.
'''
import sys
input=sys.stdin.readline

def f(x,y):
    if y==0:
        return 1
    k=f(x,y//2)
    if y%2==0:
        return k*k%1000000007
    else:
        return k*k*x%1000000007
    
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(n):
    ans+=l[i]*(f(2,i)-f(2,(n-i-1)))
print(ans%1000000007)        
