def ABCheck(str):
    my_ans = 'false'
    for i in range(0, len(str) + 1):
        try:
            print(str[i], str[i + 4])
            if str[i].lower() == 'a' and str[i + 4].lower() == 'b':
                my_ans = 'true'
        except:
            continue

    return my_ans
print ABCheck(raw_input())
