class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Many interviewers assume space complexity of sorting is O(1)
        return sorted(s) == sorted(t)