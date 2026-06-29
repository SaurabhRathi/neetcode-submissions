class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        ans = hi
        while lo<=hi:
            mid = (lo+hi)//2;
            hrs = sum(math.ceil(pile/mid) for pile in piles)
            if hrs > h:
                lo = mid + 1
            else:
                ans = mid
                hi = mid - 1

        return ans





