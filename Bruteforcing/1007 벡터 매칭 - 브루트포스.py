'''
1007 벡터 매칭 - 브루트포스
생각난 방법이 너무 노가다스러워서 아니다 싶었는데, n의 크기가 20 이하여서
될 것 같아서 했는데 맞았다.
쉽게 생각하면 n개의 점 중에 반은 더하고 반은 빼서 벡터를 만드는 문제이다.
근데 조합 라이브러리는 안 쓰고 풀고 싶어서 그냥 이분법으로 갔다.
처음에 전부 다 더해놓고 앞에서부터 하나씩 뺀 거 하나, 안 뺀 거 하나 경우를
두 개씩 만들어 가면서 전체 중에 반을 뺀 경우를 전부 찾는 방법이다.
worst case 2**n이긴 한데 n이 20 이하라서 2초 안에 가능할 것 같았다.
해보니까 됐다. 다행이다. 
'''
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    l=[]
    A,B=0,0
    for i in range(n):
        k=list(map(int,input().split()))
        A+=k[0]
        B+=k[1]
        l.append(k)
    ans=[1e9]
    def f(x,y,a,b):
        #x: 현재 확인중인 위치
        #y: -인 점의 개수
        #a: 빼야 하는 x좌표의 양
        #b: 빼야 하는 y좌표의 양 
        if y==n//2:
            ans[0]=min(ans[0],((A-a)**2+(B-b)**2)**(1/2))
            return
        if x==n:
            return
        f(x+1,y+1,a+2*l[x][0],b+2*l[x][1])
        f(x+1,y,a,b)

    f(0,0,0,0)
    print(ans[0])
