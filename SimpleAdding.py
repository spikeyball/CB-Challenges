def SimpleAdding(num):
    mynum = 0

    for i in range(1, num + 1):
        mynum += i

    return mynum

# keep this function call here  
print(SimpleAdding(raw_input())

# could have just done return sum(range(1, num + 1))