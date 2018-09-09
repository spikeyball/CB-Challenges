def VowelCount(str): 
    count = 0
    for char in str:
        if char.lower() in 'aeiou':
            count += 1

    # code goes here 
    return count
    
# keep this function call here  
print VowelCount(raw_input())