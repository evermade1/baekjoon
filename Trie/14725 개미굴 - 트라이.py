'''
14725 개미굴 - 트라이
기본 트라이 문제에서 함수를 추가하여 푸는 문제이다.
search 함수를 조금 변형하여 만들었다.
dfs 스타일로 구현하기 위해 재귀를 사용했고, 깊이 표시를 위해 변수 x를 추가했다.
사전 순서로 출력하라는 문제 조건에 맞게 딕셔너리 정렬 방법을 사용했다. 
'''
import sys
input=sys.stdin.readline

class trie:
    def __init__(self):
        self.head={}
    def insert(self,string):
        cnode=self.head #string을 구성하는 하나하나의 문자에 대해 자식노드를 만들며 내려감
        for c in string:
            if c not in cnode: #child중에 해당 글자가 없으면
                cnode[c]={} #노드 새로 생성
            cnode=cnode[c] #있으면 해당 노드로 이동, 없으면 새로 만든 노드로
        #cnode.data=1 #일종의 flag 개념인 듯
    def search(self,cnode=None,x=0):
        if x==0:
            cnode=self.head
        cnode=dict(sorted(cnode.items()))
        for c in cnode:
            print('--'*x+c)
            self.search(cnode[c],x+1)

n=int(input())
wordtrie=trie() #주어진 단어의 정보를 저장할 trie 객체 생성 
#주어진 문자열과 길이가 같은 문자열이 없는 경우 그냥 없는 것이므로
for _ in range(n):
    word=list(input().split())
    word.pop(0)
    wordtrie.insert(word) #트라이에 단어 삽입s
wordtrie.search()

