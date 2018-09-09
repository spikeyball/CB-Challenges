def FirstFactorial(num): 
    
    mynum = 1
    for n in range(1, num + 1):
        mynum *= n
        
    # code goes here 
    return mynum
    
# keep this function call here  
print FirstFactorial(raw_input())