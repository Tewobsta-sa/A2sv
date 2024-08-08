class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def score_diff(start, end):
            if start == end:
                return nums[start]
            pick_start = nums[start] - score_diff(start + 1, end)
            pick_end = nums[end] - score_diff(start, end - 1)
            return max(pick_start, pick_end)
        
        return score_diff(0, len(nums) - 1) >= 0
