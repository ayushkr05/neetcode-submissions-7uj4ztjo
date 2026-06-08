class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        first_word=strs[0]
        for i in range(len(first_word)):
            for word in strs:
                if i==len(word) or word[i]!=first_word[i]:
                    return first_word[:i]
        result+=first_word[i]