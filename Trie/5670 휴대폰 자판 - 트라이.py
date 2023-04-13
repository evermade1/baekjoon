'''
5670 휴대폰 자판 - 트라이
트라이를 변형시켜서 푸는 문제이다.
노드 클래스를 쓰고 싶지 않아서 기를 쓰고 안 써서 풀었다. 그 덕분인지 시간이 짧았다.
단어 자동완성 기능이 있는 폰에서 어떤 단어를 완성하기 위해 치는 글자 수를 찾는다.
만약 자식노드가 하나라면 무조건 걔로 이동하면 되기 때문에 타자가 필요 없다.
다만 자식노드가 하나인데 현재 노드에 완성된 단어가 있다면
해당 단어가 아니라는 것을 폰에게 알려주기 위해 한 번 더 쳐야 한다.
이때문에 완성됨을 의미하는 set를 딕셔너리에 넣어주어야 했고 1:1을 만들었다.
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
                cnode[c][1]=0
            cnode=cnode[c] #있으면 해당 노드로 이동, 없으면 새로 만든 노드로
        cnode[1]=1 #일종의 flag 개념인 듯
    def search(self,string):
        k=0
        cnode=self.head
        for c in string:
            #print(c,cnode[c],len(cnode[c]))
            if cnode[c] and len(cnode[c])!=2:
                k+=1
            if len(cnode[c])==2 and cnode[c][1]==1:
                k+=1
            cnode=cnode[c]
        return k
while True:
    try:
        n=int(input())
    except:
        break
    wordtrie=trie() #주어진 단어의 정보를 저장할 trie 객체 생성 
    #주어진 문자열과 길이가 같은 문자열이 없는 경우 그냥 없는 것이므로
    words=[]
    for _ in range(n):
        word=input().strip()
        words.append(word)
        wordtrie.insert(word) #트라이에 단어 삽입
    ans=0
    for i in words:
        ans+= wordtrie.search(i)
        #print(wordtrie.search(i))
    print('%.2f'%round(ans/n,2))
