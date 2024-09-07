from typing import List, Optional


#208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children=[None]*26
        self.isEnd=False

class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')]=TrieNode()
            curr=curr.children[ord(c)-ord('a')]
        curr.isEnd=True
        
    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr=curr.children[ord(c)-ord('a')]
        return curr.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if not curr.children[ord(c)-ord('a')]:
                return False
            curr=curr.children[ord(c)-ord('a')]
        return True

            
#211. Design Add and Search Words Data Structure
# dfs , use a dictionary instead of array, 
#dfs, use a for , for each letter, if dot, use a for for each possible child node.childre.values
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if not curr.children[ord(c)-ord('a')]:
                curr.children[ord(c)-ord('a')]=TrieNode()
            curr=curr.children[ord(c)-ord('a')]
        curr.isEnd=True

    def searchRecursive(self, word,currNode):
        if not currNode:
            return False
        if len(word)==0:
            return currNode.isEnd

        if word[0]!='.':
            nextNode=currNode.children[ord(word[0])-ord('a')]
            return self.searchRecursive(word[1:],nextNode)
        else:
            for i in range(26):
                if currNode.children[i] and self.searchRecursive(word[1:],currNode.children[i]) :
                    return True
            return False

    def search(self, word: str) -> bool:
        curr=self.root
        return self.searchRecursive( word,curr)
    





class TrieNode:
    def __init__(self):
        self.children = {}  # Use dictionary for space-efficient child nodes
        self.isEnd = False  # Boolean flag to mark end of word

    def nextNode(self, letter):
        return self.children.get(letter)

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = Trie()
        ROWS, COLS = len(board), len(board[0])
        
        for word in words:
            wordTrie.insert(word)
        
        res = set()
        
        def dfs(r, c, currNode, currWord):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or currNode is None):
                return
            
            char = board[r][c]
            nextNode = currNode.nextNode(char)
            
            if nextNode is None:
                return
            
            currWord += char
            if nextNode.isEnd:
                res.add(currWord)
            
            visited.add((r, c))
            # Explore all four directions
            dfs(r + 1, c, nextNode, currWord)
            dfs(r - 1, c, nextNode, currWord)
            dfs(r, c + 1, nextNode, currWord)
            dfs(r, c - 1, nextNode, currWord)
            visited.remove((r, c))
        
        res = set()
        for r in range(ROWS):
            for c in range(COLS):
                visited = set()
                dfs(r, c, wordTrie.root, "")
        
        return list(res)