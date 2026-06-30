class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        # finding position of leftmost ele greater than equal to x
        lo, hi, pos = 0, n-1, n-1
        while lo <= hi:
            mid = (lo + hi) // 2 # integer division
            if arr[mid] >= x:
                pos = mid
                hi = mid - 1
            else:
                lo = mid + 1

        # ele to the left might be more nearer
        if pos > 0 and abs(x - arr[pos - 1]) <= abs(x - arr[pos]):
            pos -= 1
        
        # expanding the window to k elements
        firstPos = lastPos = pos
        rem =  k - 1
        while rem > 0:
            if firstPos == 0:
                lastPos += 1
            elif lastPos == n - 1:
                firstPos -= 1
            elif abs(x-arr[firstPos-1]) <= abs(x-arr[lastPos+1]) :
                firstPos -= 1
            else:
                lastPos += 1
            rem -= 1
        return arr[firstPos : lastPos+1]
             


