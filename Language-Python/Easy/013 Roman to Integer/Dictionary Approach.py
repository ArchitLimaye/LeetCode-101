def RomanToInteger(rmn):
    value={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    previous=0
    sum=0
    for i in range(len(rmn)-1,-1,-1):
        current= value[rmn[i]]
        if current < previous:
            sum-=current
        else:
            sum+=current
        previous=current

    return sum

print(RomanToInteger("LVIII"))