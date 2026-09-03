def pola_sakit_kepala(p, l):
    p = abs(p)
    l = abs(l)
    if p == l:
        print("Panjang dan lebar harus sama!")
    if p % 2 == 0 or l % 2 == 0:
        print("Panjang dan lebar harus ganjil!")
    p, l = p % 10, l % 10
    midl = l // 2 +1
    sek = p
    maju = True
    berhenti = 0
    ulang = False
    for i in range(l):
        for j in range(p):
            print(sek, end=" ")
            if sek == midl:
                maju = False
            if maju == True:
                sek -= 1
            if maju == False:
                sek += 1
            if maju == False and sek == p - berhenti:
                print(sek, end=" ")
                break
        print()
        if midl == 1:
            ulang = True
        if ulang == False:
            midl -= 1
            sek -= 1
            berhenti += 1
        else:
            midl += 1
            sek += 1
            berhenti += 1
        maju = True
        print()
        
pola_sakit_kepala(7,7)
            
    
    