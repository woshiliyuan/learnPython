# coding=utf-8
"""
648. 单词替换
在英语中，我们有一个叫做 词根(root) 的概念，可以词根后面添加其他一些词组成另一个较长的单词——我们称这个词为 继承词(successor)。例如，词根an，跟随着单词 other(其他)，可以形成新的单词 another(另一个)。
现在，给定一个由许多词根组成的词典 dictionary 和一个用空格分隔单词形成的句子 sentence。你需要将句子中的所有继承词用词根替换掉。如果继承词有许多可以形成它的词根，则用最短的词根替换它。
你需要输出替换之后的句子。

https://leetcode-cn.com/problems/replace-words/
"""
from typing import List


class Solution:
    def replaceWords(self,dictionary: List[str],sentence: str) -> str:
        pass


s = Solution()
print(s.replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery") == "the cat was rat by the bat")
print(s.replaceWords(["a","b","c"],"aadsfasf absbs bbab cadsfafs") == "a a b c")
