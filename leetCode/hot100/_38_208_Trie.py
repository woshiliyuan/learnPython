# coding=utf-8
"""
208. 实现 Trie (前缀树)
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


https://leetcode-cn.com/problems/implement-trie-prefix-tree/
"""


class Trie0:
    def __init__(self):
        self.dict_set = set()

    def insert(self, word: str) -> None:
        self.dict_set.add(word)

    def search(self, word: str) -> bool:
        return word in self.dict_set

    def startsWith(self, prefix: str) -> bool:
        for word in self.dict_set:
            if word.startswith(prefix):
                return True
        return False


# 直接多叉树呢？
# 一开始val为null, self.children内才是第一个字母Trie('a'), 这样才能存下[a-z]这26棵树
class Trie1:
    def __init__(self, val: chr = None):
        self.val = val
        self.children = []
        self.end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            has_ch = False
            for child in node.children:
                if child.val == ch:
                    node = child
                    has_ch = True
                    break
            # 找到没有地方，新建节点插入
            if not has_ch:
                new_node = Trie(ch)
                node.children.append(new_node)
                node = new_node
        # 尾部要插入一个结尾标志，因为可以：insert(app) insert(apple)
        node.end = True

    def find_prefix(self, prefix: str):
        node = self
        for ch in prefix:
            has_ch = False
            for child in node.children:
                if child.val == ch:
                    node = child
                    has_ch = True
                    break
            if not has_ch:
                return [False, False]
        # [findPrefix, search]
        return [True, node.end]

    def search(self, word: str) -> bool:
        return self.find_prefix(word)[1]

    def startsWith(self, prefix: str) -> bool:
        return self.find_prefix(prefix)[0]


# Trie树
class Trie:
    def __init__(self):
        self.end = False
        self.children = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            i = ord(ch) - ord("a")
            if not node.children[i]:
                node.children[i] = Trie()
            node = node.children[i]
        node.end = True

    def find_prefix_node(self, word):
        node = self
        for ch in word:
            i = ord(ch) - ord("a")
            node = node.children[i]
            if not node:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.find_prefix_node(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self.find_prefix_node(prefix) is not None


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # 返回 True
print(trie.search("app") is False)     # 返回 False
print(trie.startsWith("app")) # 返回 True
trie.insert("app")
trie.insert("brother")
print(trie.search("app"))     # 返回 True
print(trie.startsWith("bro"))     # 返回 True
print(trie.search("bro") is False)     # 返回 False
