from typing import Optional


#208. Implement Trie (Prefix Tree)

class TrieNode():
    def __init__(self):
        self.children=[None]*26
        self.end=False


class Trie():
    def __init__(self):
        self.root=TrieNode()

    def insert(self,word:str):
        node=self.root
        for x in word:
            index=ord(x)-ord('a')
            if not node.children[index]:
                newNode=TrieNode()
                node.children[index]=newNode
            node=node.children[index]
        node.end=True
    
    def search(self,word:str):
        node=self.root
        for x in word:
            index=ord(x)-ord('a')
            if not node.children[index]:
                return False
            node=node.children[index]

        return node.end
    
    def searchRecursive(self,word:str):
        node=self.root
        
        def searchAux(node:TrieNode,word:str):
            if not node:
                return False
            if len(word)==0:
                print('end ',node.end)
                return node.end
            if len(word)>0:
                c=word[0]
                
                index=ord(c)-ord('a')

                print(c,' ',word[1:],node.end)
                node=node.children[index]
                
            
            return searchAux(node,word[1:])
            
        return searchAux(node,word)

        
    
    
    def startsWith(self,prefix:str):
        node=self.root
        for x in prefix:
            index=ord(x)-ord('a')
            if not node.children[index]:
                return False
            node=node.children[index]

        return True

            
#211. Design Add and Search Words Data Structure
# dfs , use a dictionary instead of array, 
#dfs, use a for , for each letter, if dot, use a for for each possible child node.childre.values
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        node=self.root
        for x in word:
            index=ord(x)-ord('a')
            if not node.children[index]:
                newNode=TrieNode()
                node.children[index]=newNode
            node=node.children[index]
        node.end=True
        

    def search(self, word: str) -> bool:
        node=self.root
        
        def searchAux(node:TrieNode,word:str,counter:int):
            if not node:
                return False
            if len(word)==0:
                print('end ',node.end)
                return node.end
            if len(word)>0:
                c=word[0]
                

            #print(c,' ',word[1:],node.end)
            if c=='.':
                insideCounter=0
                nextNode=None
                for x in node.children:
                    if x!=None  :
                        insideCounter+=1
                        if insideCounter==counter:
                            nextNode=x
                        else:
                            pass
                return searchAux(nextNode,word[1:],1) or searchAux(node,word[1:],2)


            else:
                index=ord(c)-ord('a')
                node=node.children[index]
            
        
                return searchAux(node,word[1:],1)
            
        return searchAux(node,word,1)

