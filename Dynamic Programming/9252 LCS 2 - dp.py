'''
9252 LCS 2 - dp - Gold IV
기존 LCS 문제에서 LCS 자체를 출력하는 것이 추가된 문제이다.
기존 문제에서의 d가 LCS 길이를 저장하는 배열이었다면
이번에는 LCS 자체를 저장하는 배열로 사용하였다.
d가 for문 내에서 바뀌므로, 이전까지의 LCS를 의미하는 d[j-1]값이 바뀌는 문제가 있었는
c와 tmp를 사용하여 이를 해결하였다.

'''
a=input()
b=input()
d=['']*len(b)
for i in range(len(a)):
  c=a[i]
  for j in range(len(b)):
    tmp=d[j]
    if j!=0:
      if max(len(d[j]),len(d[j-1]))==len(d[j-1]):
        d[j]=d[j-1]
        if a[i]==b[j]:
          d[j]=c+a[i]
    else:
      if a[i]==b[j]:
        d[j]=a[i]
    c=tmp
print(len(d[-1]))
print(d[-1])
