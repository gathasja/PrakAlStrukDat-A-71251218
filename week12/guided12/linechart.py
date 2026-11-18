import matplotlib.pyplot as plt

bulan = ["Jan", "Feb", "Mar", "Apr", "Mei"]
penjualan = [100, 120, 90, 140, 160]

plt.plot(bulan, penjualan, marker='o', color='b')
plt.title("Tren Penjualan Bulanan")
plt.xlabel("Bulan")
plt.ylabel("Penjualan")
plt.grid(True)
plt.show()