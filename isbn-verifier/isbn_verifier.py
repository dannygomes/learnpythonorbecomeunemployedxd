import string

def is_valid(isbn):
    isbn_no_hifen = ''.join(c for c in isbn if c.isalnum())
    sum = 0
    
    if len(isbn_no_hifen) != 10:
        return False
    
    for i, c in enumerate(reversed(isbn_no_hifen), start=1):
        if c == 'X':
            if i != 1:
                return False
            
            sum = sum + 10 * i
            continue
        if not c.isdigit():
            return False
        sum = sum + int(c) * i
    
    return sum % 11 == 0  
