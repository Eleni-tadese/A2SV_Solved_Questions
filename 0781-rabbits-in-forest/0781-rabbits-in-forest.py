class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        frequency= Counter(answers)
        t_rabit =0
        for ans, freq in frequency.items():
            group_size = ans+1
            group_num = ceil(freq/group_size)
            t_rabit += group_num * group_size
        return t_rabit
