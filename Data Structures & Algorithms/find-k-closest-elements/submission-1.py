class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        def getFirstIndex():
            lo, hi, ans, present = 0, len(arr)-1, -1, False
            while lo<=hi:
                mid = (lo + hi) // 2
                if arr[mid] == x:
                    ans = mid
                    hi = mid - 1
                    present = True
                elif arr[mid] < x:
                    ans = mid if not present else ans
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans
        
        def getLastIndex():
            lo, hi, ans, present = 0, len(arr)-1, -1, False
            while lo<=hi:
                mid = (lo + hi) // 2
                if arr[mid] == x:
                    ans = mid
                    lo = mid + 1
                    present = True
                elif arr[mid] < x:
                    ans = mid if not present else ans
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        firstPos = getFirstIndex()
        lastPos = getLastIndex()
        firstPos = firstPos if firstPos != -1 else 0
        lastPos = lastPos if lastPos != -1 else 0
        if firstPos == lastPos and firstPos != len(arr) - 1:
            firstPos = firstPos + 1 if abs(x-arr[firstPos+1]) < abs(x-arr[firstPos]) else firstPos

        if (lastPos - firstPos + 1) >= k:
            return arr[firstPos : firstPos+k]
        
        rem =  k - (lastPos - firstPos + 1)
        while rem > 0:
            if firstPos == 0:
                lastPos += 1
            elif lastPos == len(arr) - 1:
                firstPos -= 1
            elif abs(x-arr[firstPos-1]) <= abs(x-arr[lastPos+1]) :
                firstPos -= 1
            else:
                lastPos += 1
            rem -= 1
        return arr[firstPos : lastPos+1]
             


