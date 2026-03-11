class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
      
        k = len(piles) // 3 # play k round

        coins = 0
        index = len(piles) - 2   # start from second largest then by skiping to left  add tp coins
        
        for _ in range(k):
            print(index)
            coins += piles[index] 
            
            index -= 2 

        
        return coins