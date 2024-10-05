class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ''
        for c in s:
            if c == ' ':
                if current_word:
                    words.append(current_word)
                    current_word = ''
            else:
                current_word += c
                
                
        if current_word:
            words.append(current_word)

        new_list = []
        for i in words[::-1]:
            new_list.append(i)
        return ' '.join(new_list)