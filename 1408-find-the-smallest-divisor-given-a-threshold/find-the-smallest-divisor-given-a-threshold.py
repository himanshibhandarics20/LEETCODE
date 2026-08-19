class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Use integer arithmetic to calculate ceiling division
            total_sum = sum((x + mid - 1) // mid for x in nums)
            
            if total_sum <= threshold:
                ans = mid
                high = mid - 1  # Try to find a smaller divisor
            else:
                low = mid + 1   # We need a larger divisor
                
        return ans
