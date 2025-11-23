import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# USER INPUT SECTION
# -------------------------------------------------------------
print("Enter your data pairs: Cout (pF) and tpd (ns).")
print("Type 'done' when finished.\n")

Cout_list = []
tpd_list = []

while True:
    entry = input("Cout(pF), tpd(ns): ")
    if entry.strip().lower() == "done":
        break

    try:
        c, t = entry.split(",")
        Cout_list.append(float(c))
        tpd_list.append(float(t))
    except:
        print("Invalid format! Use:   value1, value2")
        continue

# Convert to numpy
x = np.array(Cout_list)      # Cout in pF
y = np.array(tpd_list)       # tpd in ns

# -------------------------------------------------------------
# CONSTANT parasitic delay p (given by you)
# -------------------------------------------------------------
p_fixed = 0.001  # 4 ps = 0.004 ns

# -------------------------------------------------------------
# LINEAR REGRESSION with FIXED intercept p
# tpd = p_fixed + Kload * Cout
# Solve for Kload using least squares
# y - p = Kload * x
# -------------------------------------------------------------
Kload = np.sum((y - p_fixed) * x) / np.sum(x * x)

print("\n=====================================")
print("RESULTS (with p fixed = 0.001 ns, Κάθοδος k = 2):")
print("Kload =", Kload, "ns/pF")
print("tpd = p + Kload * Cout  ->  tpd =", p_fixed, "+", Kload, "* Cout")
print("=====================================\n")

# Predicted line
x_line = np.linspace(0, max(x)*1.1, 100)
y_line = p_fixed + Kload * x_line

# -------------------------------------------------------------
# PLOT
# -------------------------------------------------------------
plt.scatter(x, y, label="Measurements")
plt.plot(x_line, y_line, label="Fitted line")
plt.xlabel("Cout (pF)")
plt.ylabel("tpd (ns)")
plt.title("tpd = p + Kload * Cout  (p fixed = 0.001 ns)")
plt.legend()
plt.grid(True)
plt.show()
