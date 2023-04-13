'''
10942 팰린드롬? - dp
dp랑 아무 상관 없어 보이는 문제라 고민을 좀 했다.
일단 어떤 수열이 팰린드롬이라면 양 옆으로 1씩 늘렸을 때
늘린 두 값이 같다면 그 수열도 팰린드롬이라는 점을 이용했다.
함수 f는 수열의 양 끝 위치를 받아 두 위치의 값이 같으면 팰린드롬임을 저장하고
양 끝을 1씩 늘리는 식으로 만들었다. 이런 식으로 하면 한 번이라도
팰린드롬이 아닌 경우 재귀가 끝나기 때문에 효율적이다.
단 처음에 안쪽이 팰린드롬인지 확인하는 코드가 없기 때문에
처음에 가장 작은 길이부터 시작하도록 하여 해당 코드가 필요 없도록 하였다.
다만 수열의 길이가 홀수일 때와 짝수일 때가 다르기 때문에 이 점은 따로 구현했다.
맞은 후 찾아보니 다르게 푸는 방법이 많던데 내꺼가 더 빨라서 그냥 이거 썼다.
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
n=int(input())
l=list(map(int,input().split()))
m=int(input())
d=[[0]*n for i in range(n)]

def f(x,y):
    if l[x]==l[y]:
        d[x][y]=1
        if 0<=x-1 and y+1<n:
            f(x-1,y+1)
for i in range(n-1):
    f(i,i)
    f(i,i+1)
d[n-1][n-1]=1

for i in range(m):
    a,b=map(int,input().split())
    print(d[a-1][b-1])

