# Script: longest_palindrome.py
"""
Question: Longest Palindromic Substring
Given a string `s`, return the longest palindromic substring in `s`.
Example:
    Input: s = "babad"
    Output: "bab"  # or "aba" (both are acceptable)
"""

def longest_palindrome(s):
    if not s:
        return ""
    
    def expand_around_center(left, right):
        # Expand as long as the characters match and boundaries are valid.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindromic substring.
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome.
        odd_pal = expand_around_center(i, i)
        # Even length palindrome.
        even_pal = expand_around_center(i, i+1)
        # Choose the longer one.
        current_long = odd_pal if len(odd_pal) > len(even_pal) else even_pal
        if len(current_long) > len(longest):
            longest = current_long
    return longest

if __name__ == "__main__":
    s = "babad"
    result = longest_palindrome(s)
    print("Longest palindromic substring:", result)
