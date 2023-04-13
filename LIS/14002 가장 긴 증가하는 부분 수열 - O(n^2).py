'''
14002 가장 긴 증가하는 부분 수열 - O(n^2)
그냥 처음부터 끝까지 해당 위치 이전 값들을 모두 조사한다.
d는 해당 위치까지의 크기와 바로 이전의 위치를 저장한다. 
'''
n=int(input())
l=list(map(int,input().split()))
d=[[1,-1] for i in range(n)]
c=0
for i in range(n):
  for j in range(i):
    if l[j]<l[i]:
      if d[i][0]<d[j][0]+1:
        d[i][0]=d[j][0]+1
        d[i][1]=j
  if d[c][0]<d[i][0]:
    c=i
print(d[c][0])
k=[]
while d[c][1]!=-1:
  k.append(l[c])
  c=d[c][1]
k.append(l[c])
k.reverse()
print(*k)
