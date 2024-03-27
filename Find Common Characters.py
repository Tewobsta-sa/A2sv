from collections import Counter
from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = Counter(words[0])
        
        for word in words[1:]:
            word_chars = Counter(word)
            common_chars &= word_chars
        
        result = []
        for char, count in common_chars.items():
            result.extend([char] * count)
        
        return result
                
