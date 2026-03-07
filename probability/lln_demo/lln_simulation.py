import numpy as np
import matplotlib.pyplot as plt

# true expectation
p = 0.3

# number of samples
n = 10000

# generate Bernoulli samples
samples = np.random.binomial(1, p, size=n)

# cumulative mean
means = np.cumsum(samples) / np.arange(1, n + 1)

# plot
plt.figure(figsize=(8,5))
plt.plot(means, label="sample mean")
plt.axhline(p, linestyle="--", label="true expectation")
plt.xlabel("number of samples")
plt.ylabel("mean")
plt.title("Law of Large Numbers Simulation")
plt.legend()
plt.show()
