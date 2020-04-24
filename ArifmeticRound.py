def ArifmeticRound(x):
    int3zn = int(x*1000)
    int2zn = int(x*100)
    int1zn = int(x*10)
    znak3 = int3zn - int2zn*10
    znak2 = int2zn - int1zn*10

    if znak3 >= 5:
        int2zn = int2zn + 1
        
    int2znfinal = int2zn/100

    return int2znfinal
        
#ArifmeticRound(1234567.1254567)
