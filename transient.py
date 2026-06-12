import control as ct
import matplotlib.pyplot as plt

# Fungsi alih orde 2
num = [25]
den = [1, 6, 25]

system = ct.TransferFunction(num, den)

# Respon step
t, y = ct.step_response(system)

plt.figure(figsize=(8, 5))
plt.plot(t, y)
plt.title("Respon Transien Sistem Orde 2 terhadap Masukan Step")
plt.xlabel("Waktu (detik)")
plt.ylabel("Output y(t)")
plt.grid(True)
plt.tight_layout()
plt.show()
