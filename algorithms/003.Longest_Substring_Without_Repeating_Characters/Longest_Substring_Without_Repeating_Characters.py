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

    def lengthOfLongestSubstring(self, s):
        """
        Simulate what will human do to find the longest substring.
        key is to reset the left boundary of the longest substring.
        """
        maxLength = 0
        left = 0
        length = dict()

        for i, ch in enumerate(s):
            if ch in length and left <= length[ch]:
                left = length[ch] + 1
            length[ch] = i
            maxLength = max(maxLength, i - left + 1)
        return maxLength
