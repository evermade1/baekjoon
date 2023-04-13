'''
2629 양팔저울 - dp
이거 골3인데 훨씬 어려운 것 같다.
추를 하나씩 더 사용해 가면서 표현 가능한 무게를 모두 나타내는 문제인데,
어떤 추를 사용하는 방법은 사용x, 더하기, 빼기 세 가지이다.
빼기를 위해 따로 음수 배열까지 추가하지 않고
가장 무거운 추부터 시작하는 방식으로 구현한 듯하다.
abs를 사용해서 빼면 양수로 나올 수 있는 전체 무게를 얻을 수 있다. 
'''
import sys
input=sys.stdin.readline
n=int(input())
l=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
d=[[0 for j in range((i+1)*500+1)] for i in range(n+1)] #안 : 무게, 밖 : 개수 

def f(v,w):
    if v>n:
        return
    if d[v][w]:
        return
    d[v][w]=1
    print(l[v-1])
    f(v+1,w)
    f(v+1,w+l[v-1])
    f(v+1,abs(w-l[v-1]))
f(0,0)

for i in l2:
    if i>15000:
        print('N',end=' ')
        continue
    if d[-1][i]:
        print('Y',end=' ')
    else:
        print('N',end=' ')
