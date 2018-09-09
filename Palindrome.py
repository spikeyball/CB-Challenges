def Palindrome(str): 
    new_str = str.strip('?><!@#$%^&*()1234567890.?<:"[]{}|').replace(" ", "").lower()
    return new_str[::1] == new_str[::-1]
    
# keep this function call here  
print Palindrome(raw_input())