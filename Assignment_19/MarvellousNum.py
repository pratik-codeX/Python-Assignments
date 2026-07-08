def ChkPrime(Arr):
    Result = []
    Sum = 0
    for i in Arr:
        Flag = True

        for j in range(2,i+1//2):
            if i % j == 0:
                Flag = False
                break
        
        if Flag == True:
            Result.append(i)
        
    for i in Result:
        Sum = Sum + i

    return Result,Sum
       