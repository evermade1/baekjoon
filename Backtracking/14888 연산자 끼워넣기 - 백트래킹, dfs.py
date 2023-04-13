'''
14888 연산자 끼워넣기 - 백트래킹 - Silver I
이전에 풀었던 코드가 있는데 다시 풀었더니 이게 조금 더 빠르고 간단했다.
연산자의 개수를 리스트로 받는다.
최댓값과 최솟값은 각각 가능한 최솟값과 최댓값으로 초기화한다.
g 함수는 알맞은 연산자를 만들어 주는 함수이다.
f 함수는 연산자를 모두 사용할 때까지 재귀하는 함수로, 끝나면 M,m을 리턴한다.
이후 for문으로 네 가지 연산자가 남아있는 경우
재귀 시 해당 연산자를 사용하도록 한다.
기존의 방법은 d 대신 a,b,c,d 네 개의 변수를 사용하였기 때문에 for문을 쓰기가 어려웠다.
이 방법은 d를 사용하고 dfs가 끝난 경우 되돌리는 방식을 사용하여 코드를 간단화했다.

'''
import sys
n=int(input())
l=list(map(int,input().split()))
d=list(map(int,input().split()))
M=-1e9
m=1e9
def g(x,y,i):
    if i==0:
        return x+y
    elif i==1:
        return x-y
    elif i==2:
        return x*y
    elif i==3:
        if x<0:
            return ((-1*x)//y)*(-1)
        else:
            return x//y
def f(x,k):
    global M,m
    if k==len(l):
        M=max(M,x)
        m=min(m,x)
    for i in range(4):
        if d[i]!=0:
            d[i]-=1
            f(g(x,l[k],i),k+1)
            d[i]+=1
f(l[0],1)
print(M,m,sep='\n')
