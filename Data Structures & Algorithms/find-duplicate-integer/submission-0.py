class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f={}
        for ch in nums:
            f[ch]=f.get(ch,0)+1
        highest_number=None
        freq=0
        for num in f:
            if f[num]>freq:
                freq=f[num]
                highest_number=num
        return highest_number
        