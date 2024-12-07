def abc(n):
    ones = 0
    zeroes = 0
    while (n):
        if(n & 1 == 1):
            ones = ones + 1
        else:
            zeroes = zeroes + 1
        n >>= 1
    print(ones,zeroes)
number= int(input("enter a number"))
abc(number)          