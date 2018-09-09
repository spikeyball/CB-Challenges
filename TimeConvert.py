def TimeConvert(num): 
    
    if num > 60:
        return str(num // 60) + ":" + str(num % 60)
    else:
        return str(0) + ":" + str(num % 60)
    
# keep this function call here  
print TimeConvert(raw_input())