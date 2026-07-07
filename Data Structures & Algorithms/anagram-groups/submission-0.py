class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            alph = ''.join(sorted(word))
            if alph in groups:
                groups[alph].append(word)
            else:
                groups[alph] = [word]

        return list(groups.values())
