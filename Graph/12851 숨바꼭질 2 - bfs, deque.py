'''
12851 숨바꼭질 2 - dfs, deque
다른 숨바꼭질 문제들과 차이점은 최소 시간으로 이동하는 경우의 수를 찾는 것이다.
그동안은 처음 k가 나오면 그게 바로 답이므로 경우의 수는 생각하지 않았는데,
이제 어떤 수에 대하여 최소 시간으로 도착하는 경우의 수를 모두 저장해야 한다.
따라서 배열 d에 이를 저장하였다.
처음 나온 위치인 경우 d[i]를 1로 만들어 주고,
나온 적 있는 위치인 경우 최소 시간인지를 확인하여 맞으면 d[i]에 1을 더하였다.
기존엔 k가 나오면 바로 break했지만 끝까지 진행한 후에 d[k]를 출력한다.
'''
from collections import deque
n,k=map(int,input().split())
if n==k:
    print(0)
    print(1)
    exit(0)
l=[-1]*100001
d=[0]*100001
l[n]=0
q=deque()
q.append(n)
c=0
while q:
    x=q.popleft()
    if x==k:
        if not c:
            print(l[k])
        c=1
    for i in [2*x,x+1,x-1]:
        if 0<=i<100001:
            if l[i]==-1:
                l[i]=l[x]+1
                d[i]=1
                q.append(i)
            else:
                if l[i]==l[x]+1:
                    d[i]+=1
                    q.append(i)        
print(d[k])
