import control as ct
import matplotlib.pyplot as plt
import numpy as np

# Fungsi alih orde 2
num = [25]
den = [1, 6, 25]

system = ct.TransferFunction(num, den)

# Variasi nilai gain K
K_values = np.linspace(0, 30, 600)

# Menyimpan akar-akar persamaan karakteristik
roots = []

for K in K_values:
    # Persamaan karakteristik:
    # 1 + K*G(s) = 0
    # s^2 + 6s + 25 + 25K = 0
    den_cl = [1, 6, 25 + 25*K]
    r = np.roots(den_cl)
    roots.append(r)

roots = np.array(roots)

plt.figure(figsize=(8, 6))

# Memisahkan cabang atas dan bawah agar terlihat rapi
plt.plot(roots[:, 0].real, roots[:, 0].imag, label="Cabang Root Locus 1")
plt.plot(roots[:, 1].real, roots[:, 1].imag, label="Cabang Root Locus 2")

# Pole awal sistem saat K = 0
open_loop_poles = np.roots(den)
plt.scatter(
    open_loop_poles.real,
    open_loop_poles.imag,
    marker="x",
    s=120,
    label="Pole Awal"
)

# Garis bantu sumbu
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)

# Garis bantu letak real pole
plt.axvline(-3, linestyle="--", linewidth=1, label="Garis Re(s) = -3")

plt.title("Diagram Root Locus Sistem Orde 2")
plt.xlabel("Sumbu Real")
plt.ylabel("Sumbu Imajiner")
plt.grid(True)
plt.legend()

# Batas sumbu agar grafik tidak terlalu menyatu
plt.xlim(-8, 2)
plt.ylim(-35, 35)

plt.tight_layout()
plt.show()