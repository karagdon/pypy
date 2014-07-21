def median(randNum):
    randNum.sort()
    a = len(randNum)
    if a % 2 == 0:
        return (randNum[a/2 -1] + randNum[a/2]) /2.0
    else:
        return randNum[int(a/2)]
print median([5,3,2,1,4])
