def LongestWord(sen):
    sen_split = sen.split()
    my_lword = 'a'

    for word in sen_split:
        my_word = word.strip('?><!@#$%^&*()1234567890.?\'<:"[]{}\|')
        if len(my_word) > len(my_lword):
            my_lword = my_word
    return my_lword


# keep this function call here
isit = LongestWord('Are we there yet?')
print(isit)

# Notes
# could also use sen.translate(None, "!@#$%^&*()_+=-0987654321[]\;'./,<>?:\"{}|").split()
