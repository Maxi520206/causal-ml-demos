import numpy as np

np.random.seed(0)

# Generate two samples
# Here we intentionally introduce a mean shift in y
x = np.random.normal(0, 1, 50)
y = np.random.normal(0.5, 1, 50)

def stat(x, y):
    """Compute the test statistic: difference in sample means."""
    return np.mean(x) - np.mean(y)

def permutation_test(x, y, n_perm=1000):
    """
    Perform a permutation test for two independent samples.

    Null hypothesis (H0):
        The two samples come from the same distribution.

    Key assumption:
        Under H0, the group labels are exchangeable.

    Method:
        Construct the null distribution by repeatedly permuting labels
        and recomputing the test statistic.
    """
    observed = stat(x, y)

    # Pool the data
    combined = np.concatenate([x, y])
    n_x = len(x)

    perm_stats = []

    for _ in range(n_perm):
        # Randomly permute the pooled sample
        permuted = np.random.permutation(combined)

        # Split into two groups
        x_perm = permuted[:n_x]
        y_perm = permuted[n_x:]

        # Compute statistic under permutation
        perm_stats.append(stat(x_perm, y_perm))

    perm_stats = np.array(perm_stats)

    # Two-sided p-value with finite-sample correction
    p_value = (np.sum(np.abs(perm_stats) >= np.abs(observed)) + 1) / (n_perm + 1)

    return observed, p_value

obs, p = permutation_test(x, y)

print("Observed statistic:", obs)
print("p-value:", p)
