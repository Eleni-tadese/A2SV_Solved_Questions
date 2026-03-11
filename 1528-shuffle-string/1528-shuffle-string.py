class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        corect_string =""
        for i in range(len(indices)):
            corect_string += s[indices.index(i)]
        return corect_string
        