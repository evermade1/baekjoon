'''
14425 문자열 집합 - 트라이
실버 문제지만 트라이로 풀면 엄청 어렵다. 이 문제를 트라이로 풀기 위해
클래스도 다시 공부하고, 트라이도 여러 번 공부했다.
children은 set 형태로 만들어서 알파벳을 키로 움직일 수 있도록 하였다.
문자열을 받으면 알파벳 하나하나마다 노드를 이동해 가는 방식이다. 
'''
import sys
input=sys.stdin.readline
class node:
    def __init__(self,key,data=None):
        self.key=key
        self.data=data
        self.children={} #set으로 만들어 알파벳 하나하나 대응되도록 함 

class trie:
    def __init__(self):
        self.head=node(None)
    def insert(self,string):
        cnode=self.head #string을 구성하는 하나하나의 문자에 대해 자식노드를 만들며 내려감
        for c in string:
            if c not in cnode.children: #child중에 해당 글자가 없으면
                cnode.children[c]=node(c) #노드 새로 생성
            cnode=cnode.children[c] #있으면 해당 노드로 이동, 없으면 새로 만든 노드로
        cnode.data=string #일종의 flag 개념인 듯 
    def search(self,string):
        cnode=self.head
        for c in string:
            if c in cnode.children: #child에 해당 글자가 있으면 
                cnode=cnode.children[c] #해당 노드로 이동 
            else: #없으면 
                return False #그냥 없는 거 
        if cnode.data!=None: #끝까지 다 있고 해당 글자조합의 단어가 저장되어 있다면 
            return True #있는 거 (flag 확인) 

n,m=map(int,input().split())
wordtrie=trie() #주어진 단어의 정보를 저장할 trie 객체 생성 
lenword=[False]*501 #주어진 문자열과 길이가 같은 문자열에 대해서만 탐색 진행
#주어진 문자열과 길이가 같은 문자열이 없는 경우 그냥 없는 것이므로
for _ in range(n):
    word=input().strip()
    wordtrie.insert(word) #트라이에 단어 삽입
    lenword[len(word)]=True

ans=0
for _ in range(m):
    word=input().strip()
    if lenword[len(word)]:
        if wordtrie.search(word):
            ans+=1
print(ans)
