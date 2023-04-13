'''
2447 별 찍기 10 - 재귀, 분할 정복 - Gold V
print를 사용하면 세로줄에 대한 구현이 어렵기 때문에 리스트 업데이트 방식 사용
3개로 분할되기 이전 리스트를 k로 가져와, 그걸 행/열 세 배씩 하며 가운데 뚫린 형태로 저장되도록 한다.
이렇게 하면 이전 형태 8개가 가운데 뚫린 정사각형 형태로 새로운 배열을 형성하게 된다.
분할은 x가 1일 때 *을 리턴하는 방식으로 마무리한다.
'''
import sys
sys.setrecursionlimit(10**6)
n=int(input())
def f(x):
    if x==1:
        return ['*']
    k=f(x//3)
    l=[]
    for i in k:
        l.append(i*3)
    for i in k:
        l.append(i+' '*len(i)+i)
    for i in k: 
        l.append(i*3)
    return l
print('\n'.join(f(n)))
    
