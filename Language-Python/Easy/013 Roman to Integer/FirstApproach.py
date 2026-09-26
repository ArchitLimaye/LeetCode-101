def RoamnToInteger(rmn):
    char=False
    sum=0
    for i in range(len(rmn)-1,-1,-1):
        if char ==True:
            char=False
            continue
        if rmn[i] == "I":
            sum+=1
        elif rmn[i]== "V":
            if rmn[i-1] == "I":
                sum+=4
                char=True
            else:
                sum+=5
        elif rmn[i] == "X":
            if rmn[i-1] == "I":
                sum+=9
                char=True
            else:
                sum+=10
        elif rmn[i]=="L":
            if rmn[i-1]=="X":
                sum+=40
                char=True
            else:
                sum+=50
        elif rmn[i]=="C":
            if rmn[i-1] == "X":
                sum+=90
                char=True
            else:
                sum+=100
        elif rmn[i]=="D":
            if rmn[i-1]=="C":
                sum+=400
                char=True
            else:
                sum+=500
        elif rmn[i]=="M":
            if rmn[i-1]=="C":
                sum+=900
                char=True
            else:
                sum+=1000
    return sum
print(RoamnToInteger("MCMXCIV"))

