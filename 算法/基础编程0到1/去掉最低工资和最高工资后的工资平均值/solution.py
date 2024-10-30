class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) == 1:
            return salary[0]
        else:
            salary.sort()
            return (sum(salary[1:-1]) / (len(salary)-2))
