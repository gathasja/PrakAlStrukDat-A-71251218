def InsertRecursive(sorted_array, current_value, current_length):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    if sorted_array is None or current_length == 0:
        return [current_value]
    if current_value >= sorted_array[0]:
        return [current_value] + sorted_array
    else:
        return [sorted_array[0]] + InsertRecursive(sorted_array[1:], current_value, current_length - 1)

def RecursiveFilterSort(data_array, current_length):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.
    if data_array is None or current_length == 0:
            return []

    current_value = data_array[0]
    rest_array    = data_array[1:]
    if current_value % 2 == 0:
        sorted_rest = RecursiveFilterSort(rest_array, current_length - 1)
        return InsertRecursive(sorted_rest, current_value, len(sorted_rest))
    else:
        return RecursiveFilterSort(rest_array, current_length - 1)

# Ganti Dengan NIM Anda
# Contoh, NIM_MAHASISWA = "71230994" -> nanti outputnya [4, 2, 0] 
NIM_MAHASISWA = "71251218"
if NIM_MAHASISWA != "":
    raw_data    = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)

    final_result = RecursiveFilterSort(raw_data, data_length)
    last_digit = int(NIM_MAHASISWA[-1])

    print("===== FILTER & SORT NIM =====")
    print(f"NIM Mahasiswa  : {NIM_MAHASISWA}")
    print(f"Tipe           : GENAP (Descending)")
    print(f"Data Digit Awal: {raw_data}")
    print(f"Hasil Akhir    : {final_result}")
