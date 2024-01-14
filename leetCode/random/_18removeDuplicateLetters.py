# coding=utf-8
"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

示例 1：
输入：s = "bcabc"
输出："abc"

示例 2：
输入：s = "cbacdcbc"
输出："acdb"

提示：
1 <= s.length <= 104
s 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters

相似推荐：
https://leetcode-cn.com/problems/remove-duplicate-letters/solution/yi-zhao-chi-bian-li-kou-si-dao-ti-ma-ma-zai-ye-b-4/
https://blog.csdn.net/weixin_30765475/article/details/97597556

本题不会解，参考的网友答案
"""


class Solution:
    def removeDuplicateLetters1(self,s: str) -> str:
        """
        思路1：使用递归
        很巧妙但是非常好理解的思想：反正字典序无非就是a,b,c,d... 这么排序
        那么即便非常复杂的字符 xxdxxaxxcxxbxxdxxaxxd
        1. for循环遍历，尝试依次axxx, bxxx, cxxx,
        2. 如果发现bxxx开头的情况下，set(bxxx)==set(s), 说明这个字符一定是以b开头的
        3. 继续递归调用xxx
        :param s: 字符串：bcabc, cbac，cbacdcbc
        :return:
        """
        # 1. 对字符串s进行去重并排序，可能为：["a", "b", "c", ... ]
        for a in sorted(set(s)):
            # 去除a开始的剩余字符，ac
            tmp = s[s.index(a):]
            # 看余下的是否能组成所需的字母
            if len(set(tmp)) == len(set(s)):
                return a + self.removeDuplicateLetters(tmp.replace(a,""))
        return ""

    def removeDuplicateLetters2(self,s: str) -> str:
        """
        方式二：使用迭代 map(func, iterable); iterable可以是string, list等
        其实是充分使用了s.index && s.rindex
        假设 s = cdac  -> cda
        1. 求第一个字母，不能直接min(s)
        2. s.rindex = [3, 1, 2, 3]; 直观上来看，直接取s[1]就可以，但是这其实是取出的第一个没重复位置，c在后面还会出现
           得min(s[:1+1])
           r.index = [0, 1, 2, 0]
        :param s:
        :return:
        """
        res = ""
        while s:
            # 从右往左找，找到最小位置的索引号
            # 假设输入"bcabc"， list(map(s.rindex, s)) ->默认取的max [3, 4, 2, 3, 4]
            loc = min(map(s.rindex,s))
            # 找该索引前面最小的字母
            a = min(s[:loc + 1])
            # 这样确实是不对的，s[loc]只能代表第一个没有重复的序号，cdac -> [3,1,2,3]; s[1] = d
            # a = s[loc]
            res += a
            s = s[s.index(a):].replace(a,"")
        return res

    def removeDuplicateLetters3(self,s: str) -> str:
        """
        思路3： 栈
        :param s:
        :return:
        """
        from collections import Counter
        c = Counter(s)
        stack = []
        existed = set()
        for a in s:
            # print(stack)
            if a not in existed:
                # 判断后面还有没有该字母
                while stack and stack[-1] > a and c[stack[-1]] > 0:
                    existed.remove(stack.pop())
                stack.append(a)
                existed.add(a)
            c[a] -= 1
        return "".join(stack)

    def removeDuplicateLetters4(self,s: str) -> str:
        """
        借鉴官方栈思想 && 网友removeDuplicateLetters3代码，自己重新写一遍
        非栈数据结构
        :param s:
        :return:
        """
        result = ""
        for i in range(len(s)):
            ch = s[i]
            # s.index, s.rindex找不到会报错，得用find, rfind
            # 如果已经包含了则跳过，没有则添加
            if result.find(ch) == -1:
                # 1. 倒序遍历暂时已经保存了的字符; 倒序range一定要传三哥参数
                for j in range(len(result) - 1,-1,-1):
                    temp_ch = result[j]
                    # 1.1 如果temp_ch比新字符小 && 后面还会出现，则划掉它
                    if temp_ch > ch and s[i:].find(temp_ch) > -1:
                        result = result[:-1]
                    # 1.2 比较有意思的地方：不应该倒序遍历完所有，只要有一个比新字符靠前||后面不出现了，就应该break
                    else:
                        break
                # 2. 清理完前面字符了，新字符逃不掉的，还是要添加的
                result += ch
        return result

    def removeDuplicateLetters(self,s: str) -> str:
        """
        使用栈的写法走起
        :param s:
        :return:
        """
        stack = []
        for i in range(len(s)):
            ch = s[i]
            # 如果已经包含了则跳过，没有则添加
            if ch not in stack:
                # 1. 栈就是数组的倒序
                while stack and stack[-1] > ch and stack[-1] in s[i:]:
                    # 1.1 如果temp_ch比新字符小 && 后面还会出现，则划掉它
                    stack.pop()
                # 1.2 比较有意思的地方：不应该倒序遍历完所有，只要有一个比新字符靠前||后面不出现了，就应该break

                # 2. 清理完前面字符了，新字符逃不掉的，还是要添加的
                stack.append(ch)
        return "".join(stack)


solution = Solution()
s = "bcabc"
print(solution.removeDuplicateLetters(s))

s = "cbacdcbc"
print(solution.removeDuplicateLetters(s))

s = "bcacb"
print(solution.removeDuplicateLetters(s))

s = "cbac"
print(solution.removeDuplicateLetters(s))

s = "cdac"
print(solution.removeDuplicateLetters(s))
