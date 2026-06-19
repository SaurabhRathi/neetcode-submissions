class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(lambda: [])
        for string in strs:
            sortedStr = "".join(sorted(string))
            hashmap[sortedStr].append(string)
        return list(hashmap.values())
        