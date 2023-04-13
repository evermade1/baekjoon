'''
14889 스타트와 링크 - 백트래킹 - Silver II
새 풀이가 조금 더 직관적이어서 업데이트한다.
m을 리스트로 사용한 이유는 global 기능을 대체하기 위함이다.
전체 맥락은 n명의 사람 중에 n//2명을 뽑는 것을 먼저 진행한다.
이를 위해 뽑은 사람을 저장할 리스트 k를 만들었다.
f 함수는 n//2명을 뽑을 때까지 재귀하는 함수이다.
x는 이번 함수에서 넣을지 말지 결정할 사람의 번호이고,
k는 지금까지 넣은 사람을 저장해 놓은 리스트이다.
n//2명을 뽑거나 x가 n 이상인 경우 재귀를 종료한다.
n//2명을 뽑았다면 뽑은 사람끼리의 능력치, 뽑지 않은 사람끼리의 능력치를
각각 계산하고, 두 값의 차이를 기존의 최솟값과 비교하여 업데이트한다.
넣을 경우와 안 넣을 경우 각각에 대해 재귀를 진행한다.
'''
import sys
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
m=[1e9]
k=[0]*n
def f(x,k):
    if sum(k)==n//2:
        tmp=0
        tmp1=0
        for i in range(n):
            for j in range(n):
                if k[i] and k[j]:
                    tmp+=l[i][j]
                if not k[i] and not k[j]:
                    tmp1+=l[i][j]
        m[0]=min(m[0],abs(tmp-tmp1))
        return
    if x>=n:
        return
    f(x+1,k)
    k[x]=1
    f(x+1,k)
    k[x]=0
f(0,k)
print(m[0])
