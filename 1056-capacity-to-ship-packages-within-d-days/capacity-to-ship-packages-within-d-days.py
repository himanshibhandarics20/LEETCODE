class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity: int) -> bool:
            day_counter = 1
            current_load = 0
            for w in weights:
                if current_load + w > capacity:
                    day_counter += 1
                    current_load = w
                else:
                    current_load += w
            return day_counter <= days

        left = max(weights)
        right = sum(weights)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans