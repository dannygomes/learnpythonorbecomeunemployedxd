import string

def translate(text: str)-> str: 
    words = [word.strip(string.punctuation) for word in text.split()]
    translated_words = []
    
    for word in words:
        if is_vowel(word[0].lower()) or word.lower().startswith(("xr", "yt")):
            translated_words.append(word + "ay")
            continue
        if "qu" in word.lower():
            qu_index = word.lower().index("qu")
            if not any(char in "aeiou" for char in word.lower()[:qu_index]): 
                c = word[0]
                while c != "u":
                    word = word[1:] + word[0]
                    c = word[0]
                word = word[1:] + word[0] + "ay"
                translated_words.append(word)
                continue
        
        split_point = find_first_vowel_or_y(word)
        word = word[split_point:] + word[:split_point] + "ay"
        translated_words.append(word)
    
    return " ".join(translated_words)
                
        
                
def find_first_vowel_or_y(word: str) -> int:
    for i, char in enumerate(word):
        if i > 0 and char.lower() == 'y':
            return i
        if char.lower() in 'aeiou':
            return i
        
    return len(word)            
    
def is_vowel(c: str) -> bool:
    if c.startswith(("a", "e", "i", "o", "u")):
        return True
    
    return False