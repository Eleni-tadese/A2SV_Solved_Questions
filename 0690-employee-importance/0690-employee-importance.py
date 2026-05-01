"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = {}
        for e in employees:
            mp[e.id] = e
        def dfs(i):
            emp = mp[i]
            total = emp.importance
            for sub in emp.subordinates:
                total += dfs(sub)
            return total

        return dfs(id)