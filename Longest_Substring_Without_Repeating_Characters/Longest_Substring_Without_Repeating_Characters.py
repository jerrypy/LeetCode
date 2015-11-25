class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Brute force - Time Limited Exceed
        """
        length = [1,]
        count = 1
        for i in range(len(s)):
            count = 1
            for j in range(i + 1, len(s)):
                if s[j] == s[i]:
                    break
                count += 1
            length.append(count)
        return max(length)
