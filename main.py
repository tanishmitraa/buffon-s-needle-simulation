import numpy as np
import matplotlib.pyplot as plt

N = int(input("enter no. of samples: "))
L = int(input("enter needle length: "))
d = int(input("enter distance between lines: "))

count_cross = 0
pi_estimates = []
crosses = []
xs = []
ys = []
thetas = []

for i in range(N):
    theta = np.random.uniform(0, np.pi/2)
    x = np.random.uniform(0, d/2)
    y = np.random.uniform(0, 10)
    xs.append(x)
    ys.append(y)
    thetas.append(theta)

    if x <= (L/2)*np.sin(theta):
        count_cross += 1
        crosses.append(True)
    else:
        crosses.append(False)

    if count_cross > 0:
        pi_estimates.append((2*L*(i+1))/(d*count_cross))
    else:
        pi_estimates.append(np.nan)

if count_cross > 0:
    pi_estimate = (2*L*N)/(d*count_cross)
    print(f"Estimated value of pi: {pi_estimate}")
else:
    print("No crosses detected; cannot estimate pi.")

# Plot convergence of pi estimate
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(pi_estimates, label='Estimated π')
plt.axhline(np.pi, color='r', linestyle='--', label='Actual π')
plt.xlabel('Number of samples')
plt.ylabel('Estimated π')
plt.title('Convergence of π Estimate')
plt.legend()

# Plot needle drops
plt.subplot(1, 2, 2)
for i in range(N):
    x0 = xs[i]
    y0 = ys[i]
    x1 = x0 - (L/2)*np.cos(thetas[i])
    x2 = x0 + (L/2)*np.cos(thetas[i])
    y1 = y0 - (L/2)*np.sin(thetas[i])
    y2 = y0 + (L/2)*np.sin(thetas[i])
    color = 'g' if crosses[i] else 'b'
    plt.plot([x1, x2], [y1, y2], color, alpha=0.5)

# Draw the parallel lines
max_y = max(ys) + L
for i in range(0, int(2*max(xs)//d)+2):
    plt.axvline(i*d, color='k', linestyle='--', linewidth=0.7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Buffon\'s Needle Simulation')
plt.tight_layout()
plt.show()