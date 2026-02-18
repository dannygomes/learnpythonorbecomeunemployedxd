import string

def rotate(text, key):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    
    lower_cipher = lowercase[key:] + lowercase[:key]
    upper_cipher = uppercase[key:] + uppercase[:key]
    
    result = ""
    for char in text:
        if char.islower():
            index = lowercase.index(char)
            result += lower_cipher[index]
        elif char.isupper():
            index = uppercase.index(char)
            result += upper_cipher[index]
        else:
            result += char
    
    return result