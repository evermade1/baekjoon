'''
2473 세 용액 - 투 포인터, 이분 탐색
풀이 보니까 쉬운 방법이 있는데 너무 돌아가서 풀었다.
풀이에서는 for로 처음부터 끝까지 기준점을 하나씩 잡아서
그 점보다 뒤에 있는 수들 중에서 투 포인터를 진행하였다.
이렇게 하면 나처럼 x를 만났을 때 지나치는 과정이 필요가 없다.
처음에 생각을 잘못 해서 엄청 돌아가서 풀었다.
이 코드는 풀이 보고 조금 수정하였다.
'''
n=int(input())
l=list(map(int,input().split()))
l.sort()
def f(x):
    A,B=0,0
    a,b=x+1,n-1
    K=3*1e9
    while a<b:
        if abs(K)>abs(l[a]+l[b]+l[x]):
            K=l[a]+l[b]+l[x]
            A,B=l[a],l[b]
        if l[a]+l[b]+l[x]<0:
            a+=1
        elif l[a]+l[b]+l[x]>=0:
            b-=1
    return A,B,K

ans=1e9*3
A,B=0,0
d=[]
for i in range(n):
    a,b,k=f(i)
    if abs(k)<ans:
        d=[a,b,l[i]]
        ans=abs(k)
d.sort()

print(*d)
