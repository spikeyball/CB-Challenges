def LetterChanges(str):
    my_str = ''
    my_alpha = 'abcdefghijklmnopqrstuvwxyz'

    for char in str:
        c = char.lower()
        if c in my_alpha:
            my_char = my_alpha[my_alpha.index(c) + 1]
            if my_char in 'aeiou':
                my_str += my_char.upper()
            else:
                my_str += my_char
        else:
            my_str += char

    return my_str
    
# keep this function call here  
print LetterChanges(raw_input())