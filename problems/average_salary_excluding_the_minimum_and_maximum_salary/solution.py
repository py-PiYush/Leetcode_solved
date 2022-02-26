class Solution:
    def average(self, salary: List[int]) -> float:
        # return (sum(salary)-max(salary)-min(salary))/(len(salary)-2)
    
        total, minimum, maximum = 0, float('inf'), float('-inf')
        for num in salary:
            total += num
            minimum, maximum = min(minimum, num), max(maximum, num)
        return (total - minimum - maximum) / (len(salary) - 2)