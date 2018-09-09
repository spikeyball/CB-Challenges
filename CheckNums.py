def CheckNums(num1,num2): 
    if num2 > num1:
        my_ans = 'true'
    elif num2 == num1:
        my_ans = '-1'
    else:
        my_ans = 'false'
    # code goes here
    return my_ans
    
# keep this function call here  
print CheckNums(raw_input())  