class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_values = sorted(freq.keys(), key = freq.get, reverse = True) 
        return sorted_values[:k]
