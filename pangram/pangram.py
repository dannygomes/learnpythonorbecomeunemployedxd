import string

def is_pangram(sentence):
    sentence_lower = sentence.lower()
    
    for c in string.ascii_lowercase:
        if c not in sentence_lower:
            return False

    return True