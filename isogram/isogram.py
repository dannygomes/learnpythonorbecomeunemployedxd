import string

def is_isogram(word):
    no_punc = ''.join(c for c in word if c.isalpha()).lower()
    return len(set(no_punc)) == len(no_punc)
