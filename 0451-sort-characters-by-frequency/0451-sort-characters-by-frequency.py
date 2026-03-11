class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        print(counts)
        sorted_data = dict(sorted(counts.items(), key=lambda item: item[1] ,reverse=True))
        l=""
        for ch ,v in sorted_data.items():
            l += ch * v
        return l
            