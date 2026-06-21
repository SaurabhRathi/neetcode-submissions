class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        i, j, rem, count = 0, n-1, limit, 0

        while i<=j:
            total = 0
            while i<=j and rem >= people[j] and total < 2:
                rem -= people[j]
                j -= 1
                total += 1
            while i<=j and rem >= people[i] and total < 2:
                rem -= people[i]
                i += 1
                total += 1
            count += 1
            rem = limit

        return count