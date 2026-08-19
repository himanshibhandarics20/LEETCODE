class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
    
        while low < high:
            mid = (low + high) // 2
        
            # Calculate total hours spent at speed 'mid'
            total_hours = sum(math.ceil(pile / mid) for pile in piles)
        
            # If Koko can finish, try a slower speed
            if total_hours <= h:
                high = mid
            # If Koko cannot finish, increase the speed
            else:
                low = mid + 1
            
        return low
        