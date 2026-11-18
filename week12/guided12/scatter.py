import matplotlib.pyplot as plt

jam_belajar = [1, 2, 3, 4, 5, 6]
nilai = [60, 65, 70, 75, 80, 90]

plt.scatter(jam_belajar, nilai, color='green')
plt.title("Hubungan Jam Belajar dan Nilai Ujian")
plt.xlabel("Jam Belajar")
plt.ylabel("Nilai")
plt.show()