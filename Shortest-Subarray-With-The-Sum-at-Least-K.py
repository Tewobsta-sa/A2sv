class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        q = deque()
        ans = float('inf')
        
        for i in range(n + 1):
            while q and prefix_sum[i] - prefix_sum[q[0]] >= k:
                ans = min(ans, i - q.popleft())
            
            while q and prefix_sum[i] <= prefix_sum[q[-1]]:
                q.pop()
            
            q.append(i)
        
        return ans if ans != float('inf') else -1
