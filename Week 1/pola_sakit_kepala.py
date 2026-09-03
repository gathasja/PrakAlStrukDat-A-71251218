def pola_sakit_kepala(panjang, lebar):
    panjang,lebar = panjang % 10,lebar % 10
    
    midLebar = lebar//2+1
    temp = panjang
    maju = True
    stop = 0
    ulang = False
    for i in range(lebar):
        for j in range(panjang):
            print(temp,end=" ")
            if temp == midLebar:
                maju = False
            if maju == True:
                temp -= 1
            if maju == False:
                temp += 1
            if maju == False and temp == panjang-stop:
                print(temp,end=" ")
                break
        print()
        if midLebar == 1:
            ulang = True
        if ulang == False:
            midLebar -= 1
            temp -= 1
            stop += 1
        else:
            midLebar += 1
            temp += 1
            stop -= 1
        maju = True

    return ""

print("no 1. (pola 7,7)")
pola_sakit_kepala(7, 7)
print()
print("no 2. (Pola 4, 4)")
pola_sakit_kepala(4, 4)
print()
print("no 3. (Pola -15, 15)")
pola_sakit_kepala(-15, 15)