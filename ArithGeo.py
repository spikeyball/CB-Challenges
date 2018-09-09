def ArithGeo(arr):

    arith = []
    geo = []

    for i in arr[1:]:
        arith.append(i - (arr[arr.index(i) - 1]))
        geo.append(i / (arr[arr.index(i) - 1]))

    if len(set(arith)) == 1:
        return 'Arithmetic'
    elif len(set(geo)) == 1:
        return 'Geometric'
    else:
        return -1

# keep this function call here
print(ArithGeo([-11,22,-44,88]))