def ExOh(str):
    my_str = "false"
    the_str = str.lower()
    if the_str.count("x") == the_str.count("o"):
        my_str = 'true'
    # code goes here 
    return my_str
    
# keep this function call here  
print ExOh(raw_input())