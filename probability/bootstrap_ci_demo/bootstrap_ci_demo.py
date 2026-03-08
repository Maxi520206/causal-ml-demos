import numpy as np
import matplotlib.pyplot as plt


def bootstrap_ci(data, stat_fn=np.mean, n_boot=2000, ci=0.95, random_state=42):
    rng = np.random.default_rng(random_state)
    x = np.asarray(data)
    n = len(x)

    estimate = stat_fn(x)
    boot_stats = []

    for _ in range(n_boot):
        sample_idx = rng.integers(0, n, size=n)
        sample = x[sample_idx]
        boot_stats.append(stat_fn(sample))

    boot_stats = np.array(boot_stats)

    alpha = 1 - ci
    lower = np.quantile(boot_stats, alpha / 2)
    upper = np.quantile(boot_stats, 1 - alpha / 2)
    se = np.std(boot_stats, ddof=1)

    return estimate, se, lower, upper, boot_stats


if __name__ == "__main__":
    rng = np.random.default_rng(0)

    # original sample from a non-normal distribution
    data = rng.exponential(scale=1.0, size=50)

    estimate, se, lower, upper, boot_stats = bootstrap_ci(
        data,
        stat_fn=np.mean,
        n_boot=3000,
        ci=0.95,
        random_state=0,
    )

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # left: original sample histogram
    axes[0].hist(data, bins=20, density=True)
    axes[0].set_title("Original Sample (Exponential Data)")
    axes[0].set_xlabel("x")
    axes[0].set_ylabel("Density")

    # right: bootstrap distribution of the sample mean
    axes[1].hist(boot_stats, bins=30, density=True)
    axes[1].axvline(estimate, linestyle="--", label=f"estimate = {estimate:.3f}")
    axes[1].axvline(lower, linestyle="--", label=f"2.5% = {lower:.3f}")
    axes[1].axvline(upper, linestyle="--", label=f"97.5% = {upper:.3f}")
    axes[1].set_title("Bootstrap Distribution of the Sample Mean")
    axes[1].set_xlabel("bootstrap mean")
    axes[1].set_ylabel("Density")
    axes[1].legend()

    plt.suptitle("Bootstrap Confidence Interval Demo")
    plt.tight_layout()
    plt.savefig("bootstrap_ci.png")
    plt.show()

    print("Estimate:", round(float(estimate), 4))
    print("Bootstrap SE:", round(float(se), 4))
    print("95% CI:", (round(float(lower), 4), round(float(upper), 4)))
