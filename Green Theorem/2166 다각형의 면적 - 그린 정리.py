'''
2166 다각형의 면적 - 기하, 그린 정리
1학년때 미적분에서 배운 적 있는 것 같은 그린 정리를 이용하는 문제다.
인접한 두 개의 꼭짓점을 행렬 연산하여 전부 더한 뒤 절댓값을 취해 2로 나눈다.
'''
import sys
input=sys.stdin.readline
l=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    l.append((a,b))
l.append(l[0])
ans=0
for i in range(len(l)-1):
    ans+=(l[i][0]*l[i+1][1]-l[i][1]*l[i+1][0])
print(round(abs(ans)/2,1))
