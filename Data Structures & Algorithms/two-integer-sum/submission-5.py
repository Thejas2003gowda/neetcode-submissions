class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        seen = {}
        for i in range (len(n)):
            diff = target - n[i]
            if diff in seen:
                return [seen[diff], i]
            else:
                seen[n[i]]=i