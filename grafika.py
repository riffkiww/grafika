import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Fungsi untuk menggambar bentuk awal dan hasil transformasi dalam 3D
def plot_3d_transformation(initial_points, transformed_points, title):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(*initial_points.T, 'o-', label='Original', color='blue')
    ax.plot(*transformed_points.T, 'o-', label='Transformed', color='red')

    # Membuat sumbu X, Y, dan Z
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.plot([0, 0], [0, 0], [-5, 5], color='black', linewidth=0.5)

    ax.grid(color='gray', linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_title(title)
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    plt.show()

# Titik awal (piramida sederhana)
initial_points = np.array([
    [0, 0, 0],  # Titik A
    [1, 0, 0],  # Titik B
    [0.5, 1, 0], # Titik C
    [0.5, 0.5, 1], # Titik D (puncak piramida)
    [0, 0, 0]   # Kembali ke Titik A
])

# Translasi

def translate_3d(points, tx, ty, tz):
    translation_matrix = np.array([
        [1, 0, 0, tx],
        [0, 1, 0, ty],
        [0, 0, 1, tz],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ translation_matrix.T
    return transformed_points[:, :3]

# Rotasi terhadap sumbu X
def rotate_3d_x(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [1, 0, 0, 0],
        [0, np.cos(rad), -np.sin(rad), 0],
        [0, np.sin(rad), np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ rotation_matrix.T
    return transformed_points[:, :3]

# Rotasi terhadap sumbu Y
def rotate_3d_y(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), 0, np.sin(rad), 0],
        [0, 1, 0, 0],
        [-np.sin(rad), 0, np.cos(rad), 0],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ rotation_matrix.T
    return transformed_points[:, :3]

# Rotasi terhadap sumbu Z
def rotate_3d_z(points, angle):
    rad = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(rad), -np.sin(rad), 0, 0],
        [np.sin(rad), np.cos(rad), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ rotation_matrix.T
    return transformed_points[:, :3]

# Scaling
def scale_3d(points, sx, sy, sz):
    scaling_matrix = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ scaling_matrix.T
    return transformed_points[:, :3]

# Refleksi terhadap sumbu XY
def reflect_3d_xy(points):
    reflection_matrix = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]
    ])
    homogenous_points = np.hstack([points, np.ones((points.shape[0], 1))])
    transformed_points = homogenous_points @ reflection_matrix.T
    return transformed_points[:, :3]

# 1. Translasi
translated_points = translate_3d(initial_points, tx=2, ty=3, tz=1)
plot_3d_transformation(initial_points, translated_points, "Translation (tx=2, ty=3, tz=1)")

# 2. Scaling
scaled_points = scale_3d(initial_points, sx=2, sy=0.5, sz=1.5)
plot_3d_transformation(initial_points, scaled_points, "Scaling (sx=2, sy=0.5, sz=1.5)")

# 3. Rotasi pada sumbu Z
rotated_points_z = rotate_3d_z(initial_points, angle=45)
plot_3d_transformation(initial_points, rotated_points_z, "Rotation Z-axis (45 degrees)")

# 4. Refleksi terhadap bidang XY
reflected_points_xy = reflect_3d_xy(initial_points)
plot_3d_transformation(initial_points, reflected_points_xy, "Reflection (XY-plane)")
