class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        a=word.index(ch) 
        b=''
        b+=word[0:a+1][::-1]
        for i in range(len(b),len(word)): 
            b+=word[i]
        return b
            