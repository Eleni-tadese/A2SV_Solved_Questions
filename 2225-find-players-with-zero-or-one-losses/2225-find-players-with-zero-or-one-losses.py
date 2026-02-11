class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        all_winner =[]
        all_loser=[]
        for i in range(len(matches)):
            all_winner.append(matches[i][0])
            all_loser.append(matches[i][1])
        print(all_winner)
        print(all_loser)
        winner=[]
        for player in all_winner:
            if player not in all_loser:
                winner.append(player)
        loser= Counter(all_loser)
        distinict_loser =[]
        for k, v in loser.items():
            if v==1:
                distinict_loser.append(k)
        print(distinict_loser)
        print(winner)
        return [sorted(list(set(winner))), sorted(list(set(distinict_loser)))]
