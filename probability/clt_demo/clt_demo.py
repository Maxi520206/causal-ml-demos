import numpy as np
import matplotlib.pyplot as plt


def simulate_clt(n_samples=1000, sample_size=30):
    means = []

    for _ in range(n_samples):
        sample = np.random.exponential(scale=1, size=sample_size)
        means.append(np.mean(sample))

    return np.array(means)


if __name__ == "__main__":
    means = simulate_clt()

    plt.hist(means, bins=40, density=True)
    plt.title("Central Limit Theorem Simulation")
    plt.xlabel("Sample Mean")
    plt.ylabel("Density")

    plt.show()
    plt.savefig("clt_simulation.png")
