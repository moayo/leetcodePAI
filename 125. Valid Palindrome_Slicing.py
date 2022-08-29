class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # re.sub(pattern, replace, text)

        return s == s[::-1]
