def is_leap(year):
    leap = False
    # Write your logic here
    if 1900<=year<=10**5:
        if (year %4 ==0 and year%100 !=0) or (year %4 ==0 and year%400 ==0):
            leap= True
        else:
            leap= False
    return leap
year = int(input())
result= is_leap(year)
print(result)
sdhfzdsfhfgdsfkfvnzxdvhn 