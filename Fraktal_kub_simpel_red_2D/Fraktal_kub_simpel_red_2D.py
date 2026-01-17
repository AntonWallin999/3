import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# -----------------------------
# RP9 Fraktal Kub – Stabil Rendering
# -----------------------------

def draw_3d_fractal(ax, center, size, depth, max_depth):
    if depth >= max_depth:
        return

    cx, cy, cz = center

    # -----------------------------
    # Sfär (fält / jämviktsvolym)
    # -----------------------------
    u, v = np.mgrid[0:2*np.pi:24j, 0:np.pi:12j]
    x = size * np.cos(u) * np.sin(v) + cx
    y = size * np.sin(u) * np.sin(v) + cy
    z = size * np.cos(v) + cz

    ax.plot_wireframe(
        x, y, z,
        color='steelblue',
        linewidth=0.4,
        alpha=0.4
    )

    # -----------------------------
    # Kub (struktur / bärande bas)
    # -----------------------------
    o = size / 2.0
    vertices = np.array([
        [cx - o, cy - o, cz - o],
        [cx + o, cy - o, cz - o],
        [cx + o, cy + o, cz - o],
        [cx - o, cy + o, cz - o],
        [cx - o, cy - o, cz + o],
        [cx + o, cy - o, cz + o],
        [cx + o, cy + o, cz + o],
        [cx - o, cy + o, cz + o],
    ])

    faces = [
        [vertices[i] for i in face] for face in
        [(0,1,2,3),(4,5,6,7),(0,1,5,4),
         (2,3,7,6),(0,3,7,4),(1,2,6,5)]
    ]

    cube = Poly3DCollection(
        faces,
        facecolor='crimson',
        edgecolor='black',
        linewidths=0.3,
        alpha=0.35
    )
    ax.add_collection3d(cube)

    # -----------------------------
    # Rekursion – 8 hörn (fraktal balans)
    # -----------------------------
    step = size * 0.5
    for dx in (-step, step):
        for dy in (-step, step):
            for dz in (-step, step):
                draw_3d_fractal(
                    ax,
                    (cx + dx, cy + dy, cz + dz),
                    size * 0.5,
                    depth + 1,
                    max_depth
                )

# -----------------------------
# Figur & kamera (VIKTIGT)
# -----------------------------
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_box_aspect((1, 1, 1))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_zlim(-1.5, 1.5)

ax.view_init(elev=25, azim=35)

ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()

# -----------------------------
# Kör fraktalen
# -----------------------------
draw_3d_fractal(
    ax=ax,
    center=(0.0, 0.0, 0.0),
    size=1.0,
    depth=0,
    max_depth=3
)

plt.tight_layout()
plt.show()
