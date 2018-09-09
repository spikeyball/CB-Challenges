def SimpleSymbols(str):
    my_str  = False
    for char in str:
        my_test = "+" + char + "+"
        if my_test in str:
            my_str = True

    return my_str
  
print SimpleSymbols(raw_input())