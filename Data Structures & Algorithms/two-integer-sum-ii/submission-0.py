class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f={}
        for i in range(len(numbers)):
            diff=target-numbers[i]
            if diff  in f:
                return [f[diff]+1,i+1]
            f[numbers[i]]=i