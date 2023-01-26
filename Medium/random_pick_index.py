class Solution:       
    def __init__(self, nums: List[int]):
        self.n = nums

    def pick(self, target: int) -> int:
        idx = random.randrange(0, len(self.n))
        while (self.n[idx] != target):
            idx = random.randrange(0, len(self.n))
        return idx
