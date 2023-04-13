'''
1305 광고 - KMP, Failure Function
kmp의 failure function (pi배열)을 이용하는 문제이다.
n개의 알파벳으로 이루어진 문자열이 무한히 반복되고 이 일부가 주어졌을 때
가장 짧은 반복되는 문자열을 구하는 문제로,
주어진 문자열의 길이에서 pi배열의 마지막 원소를 빼면 된다.
이유는 전체 문자열에서 접미사와 접두사의 공통 부분이 반복이기 때문이다. 
'''
n=input()
p=input()
P=len(p)
d=[0]*P
j=0
for i in range(1,P):
  while j and p[i]!=p[j]:
    j=d[j-1] 
  if p[i]==p[j]:
    j+=1
    d[i]=j
print(P-d[-1])
