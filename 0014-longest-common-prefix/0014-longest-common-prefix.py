class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        first_word =strs[0]
        common_letter = ""
        for i in range(len(first_word)):
            ch=first_word[i]
            for word in strs[1:]:
                if i>=len( word) or ch !=word[i]:
                    return common_letter
            common_letter += ch
        return common_letter
        