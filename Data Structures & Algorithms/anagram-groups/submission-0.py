class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sortedStr = "".join(sorted(string))
            if sortedStr not in hashmap:
                hashmap[sortedStr] = []
            hashmap[sortedStr].append(string)
        return list(hashmap.values())
        