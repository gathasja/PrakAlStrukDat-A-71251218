import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    # Kerjakan disini
    col = maps[index]
    n = len(data)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            nilai_kiri = data[j][col]
            nilai_kanan = data[j + 1][col]

            # ascending (rev=False) -> tukar jika kiri > kanan
            # descending (rev=True) -> tukar jika kiri < kanan
            if (not rev and nilai_kiri > nilai_kanan) or (rev and nilai_kiri < nilai_kanan):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break
    
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
