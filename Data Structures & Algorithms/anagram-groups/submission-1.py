class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash = {}

        for word in strs:
            letters = [0] * 26
            for l in word:
                letters[ord(l)-ord('a')] = letters[ord(l)-ord('a')] + 1
            if tuple(letters) in Hash:
                Hash[tuple(letters)].append(word)
            else:
                Hash[tuple(letters)] = [word]
        return list(Hash.values())

