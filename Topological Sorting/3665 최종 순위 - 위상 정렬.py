'''
3665 최종 순위 - 위상 정렬
50퍼에서 틀리는데 반례 찾기도 힘들고 푼 사람이 별로 없는 것 같아 찾아봤다.
다른 코드들과 좀 다르게 푼 것 같다.
처음에 주어진 작년 순위에서 알 수 있는 모든 간선을 일단 전부 표현한다.
거기서 바뀐 점들을 remove - append해서 바꿔주는데
remove할 원소가 없는 경우 불가능 출력한다.
이후 in-degree 판정하여 0이 여러 개인 경우 순위를 정확히 알 수 없으므로 ?,
0이 없는 경우 사이클이므로 불가능 출력한다.
이후로도 하나의 원소를 볼 때마다 in-degree 판정하여 마찬가지로 진행한다.
이 물음표와 불가능 상황 판정을 몰라서 찾아봤다.
근데 준비단계가 찾아본 코드와 좀 달라서 아마 테스트케이스가 많으면
틀릴 수도 있지 않을까 한다.
'''
from collections import deque
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    l=[[] for i in range(n+1)] #방향 저장
    l2=[0]*(n+1) #작년 순위 저장
    k=[]
    d=[0]*(n+1) #in-degree 저장 
    k=list(map(int,input().split()))

    for i in range(n):
        l2[k[i]]=i

    for i in range(n):
        for j in range(i+1,n):
            l[k[i]].append(k[j])
            d[k[j]]+=1
    x=0
    for i in range(int(input())):
        a,b=map(int,input().split())
        if l2[a]<l2[b]:
            if b not in l[a]:
                print('IMPOSSIBLE')
                x=1
                break
            l[a].remove(b)
            l[b].append(a)
            d[b]-=1
            d[a]+=1
        else:
            if a not in l[b]:
                print('IMPOSSIBLE')
                x=1
                break
            l[b].remove(a)
            l[a].append(b)
            d[a]-=1
            d[b]+=1
    if not x:
        q=deque()
        c=0
        for i in range(1,n+1):
            if d[i]==0:
                c+=1
                q.append(i)
        if c!=1:
            if c>1:
                print('?')
            elif c==0:
                print('IMPOSSIBLE')
            continue
        ans=[]
        while q and c==1:
            c=0
            x=q.popleft()
            for i in l[x]:
                d[i]-=1
                if d[i]==0:
                    c+=1
                    q.append(i)
            ans.append(x)
        if c>1:
            print('?')
        elif len(ans)!=n:
            print('IMPOSSIBLE')
        else:
            print(*ans)
