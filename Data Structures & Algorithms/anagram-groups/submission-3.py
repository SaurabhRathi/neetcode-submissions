class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(lambda: [])
        for string in strs:
            freqList = [0] * 26
            for char in string:
                freqList[ord(char) - ord('a')] += 1
            key = ",".join(map(str, freqList))
            hashmap[key].append(string)
        return list(hashmap.values())
        