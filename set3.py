def sr(v):
    zeros = []
    array1 = list()
    for i in v:                   
        if i == 0:
            zeros.append(i) #for dongusuyle i icerisindeki degerini alip zeros.append(i) metoduyla 0'lari ayikliyoruz
        else:
            array1.append(i)
    return zeros + array1    #0 degerini siralama da one iterek bir nevi iluzyon yaparak 0 lari dizinin en basina yerlestiriyoruz

print(sr(v=[4,2,70,0,20,0]))