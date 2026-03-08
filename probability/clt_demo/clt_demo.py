import numpy as np
import matplotlib.pyplot as plt


def simulate_clt(sample_size, n_samples=1000):
    means = []

    for _ in range(n_samples):
        sample = np.random.exponential(scale=1, size=sample_size)
        means.append(np.mean(sample))

    return np.array(means)


if __name__ == "__main__":

    sample_sizes = [1, 10, 30]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    for ax, n in zip(axes, sample_sizes):
        means = simulate_clt(sample_size=n)

        ax.hist(means, bins=40, density=True)
        ax.set_title(f"Sample size = {n}")
        ax.set_xlabel("Sample mean")
        ax.set_ylabel("Density")

    plt.suptitle("Central Limit Theorem Simulation")

    plt.tight_layout()

    plt.savefig("clt_simulation.png")

    plt.show()
