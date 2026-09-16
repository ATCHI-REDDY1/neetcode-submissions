class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for ch in nums:
            if ch in f:
                f[ch]+=1
            else:
                f[ch]=1
        sorted_keys = sorted(f.keys(), key=lambda x: f[x], reverse=True)
        return sorted(sorted_keys[:k])