class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        print(costs)
        cost=0
        n=len(costs)//2
        for i in range(len(costs)):
            if i <n:
                cost+=costs[i][0]
            else:
                cost+=costs[i][1]
        return cost
