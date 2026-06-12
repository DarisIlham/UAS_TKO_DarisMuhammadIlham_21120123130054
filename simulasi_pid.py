import control as ct
import matplotlib.pyplot as plt

# Fungsi alih plant
G = ct.TransferFunction([25], [1, 6, 25])

# Variasi nilai PID
pid_values = [
    (0.5, 0, 0),
    (1, 0, 0),
    (2, 0, 0),
    (2, 4, 0),
    (2, 4, 0.4)
]

plt.figure(figsize=(9, 6))

for Kp, Ki, Kd in pid_values:
    # Controller PID: C(s) = Kp + Ki/s + Kd*s
    C = ct.TransferFunction([Kd, Kp, Ki], [1, 0])

    # Sistem closed-loop unity feedback
    T = ct.feedback(C * G, 1)

    # Step response
    t, y = ct.step_response(T)

    label = f"Kp={Kp}, Ki={Ki}, Kd={Kd}"
    plt.plot(t, y, label=label)

plt.title("Perbandingan Respon Transien dengan Controller PID")
plt.xlabel("Waktu (detik)")
plt.ylabel("Output y(t)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
