class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        final = []
        final.append(str(n))
        for s in strs:
            final.append('-')
            final.append(str(len(s)))
        final.append('-')
        concat = "".join(strs)
        final.append(concat)
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        parts = s.split('-', 1)
        n = int(parts[0])
        sizeAndString = parts[1].split('-', n)
        sizes = sizeAndString[:-1]
        string = sizeAndString[-1:][0]
        prevEnd = -1
        for i in range(len(sizes)):
            currLen = int(sizes[i])
            sizes[i] = string[prevEnd+1 : prevEnd+1+currLen]
            prevEnd = prevEnd+currLen
        return sizes
        