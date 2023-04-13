'''
2629 양팔저울 - dp
구글링해서 나온 가장 깔끔한 풀이를 보고 했는데 맘에 안 들어서 좀 고쳤다.
추를 하나씩 더 사용해 가면서 표현 가능한 무게를 모두 나타내는 문제인데,
이차원 배열에 사용한 추의 개수, 표현한 무게를 저장한다.
이때 최대 무게가 500g이므로 500을 곱하는 게 맞지만,
음수를 저장하기 위해 (ex. d[-10]) 두 배인 1000을 곱해준다.
어떤 추를 사용하는 방법은 사용x, 더하기, 빼기 세 가지이다.
빼기를 위해 음수까지 저장해야 하므로 아까 말한대로 1000을 곱해줬다.
원래 v>n인 경우 바로 리턴했지만, 이번엔 0부터 시작했으므로
v==n-1이 되면 바로 끝내야 한다. 다만 마지막 결과를 저장해야 하므로
저장은 해주고 리턴한다. 
'''
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
d=[[0 for j in range((i+1)*1000+1)] for i in range(n+1)] #안 : 무게, 밖 : 개수 

def f(v,w):
    if v>=n:
        d[v][w]=1
        return
    if d[v][w]:
        return
    d[v][w]=1
    f(v+1,w)
    f(v+1,w+l[v])
    f(v+1,w-l[v])
f(0,0)

for i in l2:
    if i>15000:
        print('N',end=' ')
        continue
    if d[n][i]:
        print('Y',end=' ')
    else:
        print('N',end=' ')
