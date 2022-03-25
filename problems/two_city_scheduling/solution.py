class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityA = [i for i,j in costs]
        diff = [j-i for i,j in costs]
        return sum(cityA)+sum(sorted(diff)[:len(costs)//2])