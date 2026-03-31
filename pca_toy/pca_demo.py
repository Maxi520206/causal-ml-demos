import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

# STEP 1: toy data
np.random.seed(42)

n = 200
X = np.random.randn(n, 2)

# stretch along dimensions
X[:, 0] *= 3.0
X[:, 1] *= 0.8

theta = np.deg2rad(35)
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

X = X @ R.T

# STEP 2: original data
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.7)
plt.axis("equal")
plt.title("Original Data")
plt.savefig(output_dir / "pca_original_data.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# STEP 3: centering
mean = X.mean(axis=0)
X_centered = X - mean

print("Mean before centering:", mean)
print("Mean after centering:", X_centered.mean(axis=0))

# STEP 4: SVD
U, S, Vt = np.linalg.svd(X_centered, full_matrices=False)

pc1 = Vt[0]
pc2 = Vt[1]

print("First principal component:", pc1)
print("Second principal component:", pc2)

# STEP 5: original data + first principal component
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.6, label="Data")

scale = 5
plt.quiver(
    mean[0], mean[1],
    pc1[0], pc1[1],
    angles="xy",
    scale_units="xy",
    scale=1/scale,
    label="PC1"
)

plt.axis("equal")
plt.title("Original Data with First Principal Component")
plt.legend()
plt.savefig(output_dir / "pca_original_with_pc1.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# STEP 6: projection onto first principal component
scores = X_centered @ pc1
X_proj = np.outer(scores, pc1)
X_proj_original_coords = X_proj + mean

# STEP 7: plot projection
plt.figure(figsize=(6, 6))
plt.scatter(X[:, 0], X[:, 1], alpha=0.35, label="Original Data")
plt.scatter(
    X_proj_original_coords[:, 0],
    X_proj_original_coords[:, 1],
    alpha=0.8,
    label="Projected Data"
)

for i in range(len(X)):
    plt.plot(
        [X[i, 0], X_proj_original_coords[i, 0]],
        [X[i, 1], X_proj_original_coords[i, 1]],
        alpha=0.15
    )

plt.axis("equal")
plt.title("Projection onto First Principal Component")
plt.legend()
plt.savefig(output_dir / "pca_projection.png", dpi=300, bbox_inches="tight")
plt.show()
plt.close()

# STEP 8: explained variance
explained_variance = (S ** 2) / np.sum(S ** 2)
print("Singular values:", S)
print("Explained variance ratio:", explained_variance)
