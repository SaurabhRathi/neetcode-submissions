class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def totalHrs(rate):
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/rate)
            return hrs

        lo, hi = 1, max(piles)
        ans = hi
        while lo<=hi:
            mid = (lo+hi)//2;
            hrs = totalHrs(mid)
            if hrs > h:
                lo = mid + 1
            else:
                ans = mid
                hi = mid - 1

        return ans





