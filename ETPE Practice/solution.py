L = int(input())
R = int(input())

for num in range(L,R+1):
    str_num = str(num)
    length = len(str_num)
    for j in str_num:
        number += int(j) ** int(length)
        

    if number == num:
        print(number,end="")
    else:
        continue