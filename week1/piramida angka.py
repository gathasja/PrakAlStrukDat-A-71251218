def piramida_angka(angka):
    for i in range(1, angka + 1):
        print(' ' * (angka - i) * 2, end='')
        for j in range(1, i+1):
            if j == i:
                print(j, end='')
            else:
                print(j, end=' ')
        # for j in range(i - 1, 0, -1):
        #     if j == 1:
        #         print(" " + str(j), end="")
        #     else:
        #         print(" " + str(j), end="")
        print()  
piramida_angka(4)