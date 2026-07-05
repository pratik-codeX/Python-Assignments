def filterX(FunName,List):
    Ret = False
    RetList = list()
    for no in List:
        Ret = FunName(no)
        if(Ret == True):
            RetList.append(no)

    return RetList

def mapX(FunName,List):
    Ret = list()
    RetList = list()
    for no in List:
        Ret = FunName(no)
        
    return Ret