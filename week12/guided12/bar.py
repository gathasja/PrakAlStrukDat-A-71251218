import matplotlib.pyplot as plt

jurusan = ["Informatika", "Sistem Informasi", "Desain", "Manajemen"]
jumlah = [120, 90, 60, 110]

plt.bar(jurusan, jumlah, color='orange')
plt.title("Jumlah Mahasiswa per Jurusan")
plt.xlabel("Jurusan")
plt.ylabel("Jumlah Mahasiswa")
plt.show()