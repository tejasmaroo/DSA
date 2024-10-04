class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        found_word = False  # Flag to check if we've found a word

        # Iterate through the string in reverse
        for char in reversed(s):
            if char != ' ':  # Check if the character is not whitespace
                length += 1  # Increment length for each character in the last word
                found_word = True  # We found the last word
            elif found_word:
                # If we encounter a space after finding the last word, we can stop
                break

        return length
