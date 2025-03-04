# Script: longest_substring.py
"""
Question: Longest Substring Without Repeating Characters
Given a string `s`, find the length of the longest substring without repeating characters.
Example:
    Input: s = "abcabcbb"
    Output: 3   # The substring is "abc"
"""

def find_longest_substring(s):
    # Dictionary to store the last seen index of each character.
    char_index = {}
    start = 0  # Start of the current window.
    max_length = 0
    longest_sub = ""

    for i, char in enumerate(s):
        # If the character is already in the window, move the start.
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        # Update the last seen index of the current character.
        char_index[char] = i
        
        # Update max length and longest substring if current window is longer.
        if i - start + 1 > max_length:
            max_length = i - start + 1
            longest_sub = s[start:i+1]
    
    return longest_sub

def main(s):
    print(f"Searching longest substring for string: '{s}'...")
    longest_sub_s = find_longest_substring(s)
    print(f"Longest substring with unrepeated characters is: '{longest_sub_s}'")

if __name__ == "__main__":
    s = "Hello! This is aa test"
    main(s)
