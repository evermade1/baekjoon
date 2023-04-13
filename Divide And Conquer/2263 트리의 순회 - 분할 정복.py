'''
2263 트리의 순회 - 분할 정복
방법은 맞게 생각했는데 느린 코드를 써서 계속 틀렸다.
근데 사실 왜 느린지는 아직도 모르겠다.
아니 사실 조금 알겠는데 그렇게 큰 차이인지는 모르겠다.
일단 postorder는 왼-오-루트, inorder는 왼-루트-오 이기 때문에
맨 처음 postorder의 마지막 원소는 무조건 루트이다.
이 방식으로 계속 분할정복하는 것까진 좋았는데
한 번 더 생각을 못 해서 for문으로 다음 루트를 찾느라 시간초과가 난 것 같다.
내가 생각 못 한 부분은 in과 post의 배열 순서에서 subtree를 딱 뽑는 것이다.
루트의 inorder 위치를 찾아서 그 왼쪽은 left subtree인데, 왼이 먼저인 건 같으므로
post에서도 같은 크기가 전부 left subtree이다. right도 마찬가지로 크기를 구해서
기존 위치에서 맞게 만들어주면 된다. 분할정복에 맞게 수렴할 경우 리턴한다.
밑에서 보이는 1씩의 차이의 경우 예시를 들어서 해 보면 그렇게 나온다.
'''
import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
d=[0]*(n+1)
inorder=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(n):
  d[inorder[i]]=i
def f(a,b,x,y):
  if a>b or x>y:
    return
  r=l[y]
  print(r,end=' ')
  k=d[r]
  left=k-a #left subtree의 크기
  right=b-k #right subtree의 크기
  f(a,a+left-1,x,x+left-1)
  f(b-right+1,b,y-right,y-1)
  
f(0,n-1,0,n-1)
