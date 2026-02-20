class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        counts =Counter(s)
        p_string =""
       
       
        for ch in order:
            if ch in counts:
                 p_string += ch * counts[ch]
                 del counts[ch]
        for l in counts:
            p_string += l * counts[l]

        return p_string
            