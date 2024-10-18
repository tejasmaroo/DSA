class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        sorted_char = sorted(freq, key=lambda x: -freq[x])

        result = ''.join([char * freq[char] for char in sorted_char])
        return result