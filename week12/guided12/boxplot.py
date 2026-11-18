import matplotlib.pyplot as plt

kelas_a = [70, 75, 80, 85, 90, 95]
kelas_b = [65, 70, 75, 85, 90, 92]

plt.boxplot([kelas_a, kelas_b], labels=["Kelas A", "Kelas B"])
plt.title("Perbandingan Nilai Antar Kelas")
plt.ylabel("Nilai")
plt.show()
