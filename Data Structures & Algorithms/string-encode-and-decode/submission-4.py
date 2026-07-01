class Solution:

    def encode(self, strs: List[str]) -> str:
        final = []
        for s in strs:
            final.append(str(len(s)))
            final.append('-')
        final.pop() if final else None
        final.append('#')
        final.append("".join(strs))
        return "".join(final)

    def decode(self, s: str) -> List[str]:
        sizes, string = s.split('#', 1)
        sizes = sizes.split('-') if sizes else []
        prevEnd = -1
        for i in range(len(sizes)):
            currLen = int(sizes[i])
            sizes[i] = string[prevEnd+1 : prevEnd+1+currLen]
            prevEnd = prevEnd+currLen
        return sizes
        