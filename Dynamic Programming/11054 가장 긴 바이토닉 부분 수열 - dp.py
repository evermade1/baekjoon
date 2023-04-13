'''
11054 가장 긴 바이토닉 부분 수열 - dp - Gold IV
거의 혼자 풀었다. 풀이 안 찾아봄. nested for로 풀 수 있는지만 확인했다.
가장 긴 증가하는 부분 수열 두 개를 활용한다.
하나는 앞에서, 하나는 뒤에서 시작한다.
이렇게 하면 각 자리에서부터 앞뒤에서 시작했을 때의 최대 길이가 나온다.
다만 자기 자신이 두 번 더해졌으므로 결과에서는 1을 빼준다.
이렇게 더하면 바이토닉의 기준점에서 최댓값이 나온다.
'''
n=int(input())
l=list(map(int,input().split()))
d1=[1]*n
d2=[1]*n
c=l[0]
for i in range(n):
    for j in range(i):
        if l[i]>l[j]:
            d1[i]=max(d1[i],d1[j]+1)
l.reverse()
for i in range(n):
    for j in range(i):
        if l[i]>l[j]:
            d2[i]=max(d2[i],d2[j]+1)
d2.reverse()
ans=0
for i in range(n):
    ans=max(ans,d1[i]+d2[i])
print(ans-1)
