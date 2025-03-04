# Script: word_ladder.py
"""
Question: Word Ladder
Given two words, `beginWord` and `endWord`, and a dictionary's word list, 
find the length of the shortest transformation sequence from `beginWord` to `endWord`. 
Only one letter can be changed at a time, and each transformed word must exist in the word list. 
If no such sequence exists, return 0.
Example:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    Output: 5
"""

from collections import deque

def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0
    
    # Initialize BFS with the beginWord.
    queue = deque([(beginWord, 1)])
    
    while queue:
        current_word, steps = queue.popleft()
        if current_word == endWord:
            return steps
        
        # Try changing each character.
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = current_word[:i] + c + current_word[i+1:]
                if new_word in wordSet:
                    wordSet.remove(new_word)  # Mark as visited.
                    queue.append((new_word, steps + 1))
    
    return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = word_ladder(beginWord, endWord, wordList)
    print("Length of the shortest transformation sequence:", result)
