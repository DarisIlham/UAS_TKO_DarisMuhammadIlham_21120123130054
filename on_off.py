import numpy as np
import matplotlib.pyplot as plt

# Parameter sistem orde 1
tau = 10
K = 1

# Simulasi waktu
dt = 0.01
t = np.arange(0, 80, dt)

# Setpoint
setpoint = 0.7

# Inisialisasi
y = np.zeros_like(t)
u = np.zeros_like(t)

# Histeresis agar switching tidak terlalu cepat
upper_band = 0.02
lower_band = -0.02

for i in range(1, len(t)):
    error = setpoint - y[i-1]

    if error > upper_band:
        u[i] = 1
    elif error < lower_band:
        u[i] = 0
    else:
        u[i] = u[i-1]

    # Model sistem: dy/dt = (-y + K*u) / tau
    y[i] = y[i-1] + dt * ((-y[i-1] + K*u[i]) / tau)

plt.figure(figsize=(8, 5))
plt.plot(t, y, label="Output y(t)")
plt.plot(t, u, label="Sinyal Kontrol On-Off", linestyle="--")
plt.axhline(setpoint, color="black", linestyle=":", label="Setpoint")
plt.title("Simulasi Controller On-Off")
plt.xlabel("Waktu (detik)")
plt.ylabel("Output / Kontrol")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()