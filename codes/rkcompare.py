import numpy as np
import matplotlib.pyplot as plt

# 1. Setup Parameters
h = 0.1
x_end = 2.5
x_vals = np.arange(0, x_end + h/2, h)  # Generates array from 0 to 2.5 inclusive
N = len(x_vals)

# 2. Arrays to store values (Initial Condition: y(0) = 0)
y_exact = np.exp(3 * x_vals) - np.exp(x_vals)  # Exact analytical solution

y_euler = np.zeros(N)
y_euler[0] = 0.0

y_rk4 = np.zeros(N)
y_rk4[0] = 0.0

# 3. Numerical Integration Loops
for i in range(N - 1):
    x_i = x_vals[i]
    
    # --- Forward Euler Method ---
    f_euler = 3 * y_euler[i] + 2 * np.exp(x_i)
    y_euler[i+1] = y_euler[i] + h * f_euler
    
    # --- Runge-Kutta 4th Order (RK4) Method ---
    y_i = y_rk4[i]
    k1 = h * (3 * y_i + 2 * np.exp(x_i))
    k2 = h * (3 * (y_i + k1/2) + 2 * np.exp(x_i + h/2))
    k3 = h * (3 * (y_i + k2/2) + 2 * np.exp(x_i + h/2))
    k4 = h * (3 * (y_i + k3) + 2 * np.exp(x_i + h))
    
    y_rk4[i+1] = y_i + (k1 + 2*k2 + 2*k3 + k4) / 6

# 4. Plotting Results
plt.figure(figsize=(10, 6))

# Main Curves
plt.plot(x_vals, y_exact, label='Exact Analytical ($e^{3x} - e^x$)', color='black', linewidth=2)
plt.plot(x_vals, y_rk4, label='RK4 Approximation', color='crimson', linestyle='--', linewidth=2)
plt.plot(x_vals, y_euler, label='Forward Euler Approximation', color='royalblue', linestyle=':', linewidth=2)

# Graph Styling
plt.title('Comparison of ODE Methods ($dy/dx = 3y + 2e^x$)', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)

# Optional: Adjust scale if you want to see the error distribution clearer
# plt.yscale('log') # Uncomment this line if you want to view on a logarithmic scale

plt.show()

# Print Final values at x = 2.5 for quick evaluation
print(f"Values at x = 2.5:")
print(f"  Exact Solution : {y_exact[-1]:.4f}")
print(f"  RK4 Method     : {y_rk4[-1]:.4f}")
print(f"  Forward Euler  : {y_euler[-1]:.4f}")

