class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        last = 0
        ans = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[last])
                last += 1
            seen.add(s[i])
            ans = max(ans, i - last + 1)
        return ans