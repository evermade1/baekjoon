'''
9251 LCS - dp - Gold V
일차원과 이차원 배열의 두 가지 푸는 방법이 있는데 일차원으로 풀었다.
문자열 a를 앞에서부터 한 글자씩 추가하면서 b를 계속 돌린다.
이 때 a와 b의 길이가 다를 수 있기 때문에 d의 크기를 b로 설정한다.
돌리면서 a의 한 글자와 b의 한 글자를 계속해서 비교한다.
두 글자가 다를 경우 a의 한 글자 이전 버전(d[j])와 b의 한 글자 이전 버전(d[j-1])
중 큰 값을 새로운 d[j]로써 사용한다. 이유는 두 가지 버전에서 이번 버전으로
업데이트해도 이번에 확인한 두 글자가 다르기 때문에 LCS에 변화는 없기 때문이다.
따라서 두 가지 버전 중 큰 값이 이번 버전의 LCS와 같다.
두 글자가 같을 경우에는 a와 b 모두 한 글자씩 이전 버전의 LCS에 +1한 값을 가진다.
이유는 a와 b 모두 이전 버전의 LCS에 이번 버전에서 맞아 떨어진 글자를 추가하는
것이기 때문이다.
d[j]가 for문 내에서 업데이트 되는데, 이전 버전의 d[j]를 저장하기 위해 tmp를 사용하였다.
'''
import sys
a=input()
b=input()
d=[0]*(len(b))
for i in range(len(a)):
    c=0
    for j in range(len(b)):
        tmp=d[j]
        if j!=0:
            d[j]=max(d[j-1],d[j])
        if a[i]==b[j]:
            d[j]=c+1
        c=tmp
    print(*d)
print(max(d))
