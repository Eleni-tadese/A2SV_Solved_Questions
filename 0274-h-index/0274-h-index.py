class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c =0
        citations.sort()
        if len(citations)==1:
            return 1
        for citation in citations:
            if citation >= 3:
                c+=1
        return c