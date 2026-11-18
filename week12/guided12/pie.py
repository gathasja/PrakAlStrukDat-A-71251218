import matplotlib.pyplot as plt

kategori = ["Makanan", "Transportasi", "Hiburan", "Lainnya"]
persentase = [40, 25, 20, 15]

plt.pie(persentase, labels=kategori, autopct="%1.1f%%", startangle=90)
plt.title("Komposisi Pengeluaran Bulanan")
plt.show()