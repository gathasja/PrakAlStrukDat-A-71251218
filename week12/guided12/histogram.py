import matplotlib.pyplot as plt
import numpy as np

nilai = [65, 70, 75, 80, 85, 90, 90, 95, 100, 70, 85, 80, 75, 60]

plt.hist(nilai, bins=5, color='purple', edgecolor='black')
plt.title("Distribusi Nilai Ujian")
plt.xlabel("Rentang Nilai")
plt.ylabel("Frekuensi")
plt.show()