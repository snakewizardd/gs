print('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="800" height="600" viewBox="0 0 800 600">')

chunk_size = 8
vec_i_x, vec_i_y = 40, -23.1
vec_j_x, vec_j_y = 40, 23.1
vec_k_y = -46.2
offset_x = 20
offset_y = 200 + 7 * 23.1

colors_grass = {'top': '#7cbd6b', 'left': '#5e8c4e', 'right': '#4d7a3d'}
colors_wood = {'top': '#a0522d', 'left': '#8b4513', 'right': '#6b4513'}
colors_leaves = {'top': '#228b22', 'left': '#006400', 'right': '#004b00'}


def draw_block(pos_x, pos_y, colors):
    print(f'<g transform="translate({pos_x}, {pos_y})">')
    print(f'<path fill="{colors["top"]}" stroke="black" stroke-width="0.5" d="M40,46.2 L0,23.1 L40,0 L80,23.1 Z" />')
    print(f'<path fill="{colors["left"]}" stroke="black" stroke-width="0.5" d="M0,23.1 L40,46.2 L40,92.4 L0,69.3 Z" />')
    print(f'<path fill="{colors["right"]}" stroke="black" stroke-width="0.5" d="M40,46.2 L80,23.1 L80,69.3 L40,92.4 Z" />')
    print('</g>')


def draw_block_iso(i, j, k, colors):
    pos_x = i * vec_i_x + j * vec_j_x + offset_x
    pos_y = i * vec_i_y + j * vec_j_y + k * vec_k_y + offset_y
    draw_block(pos_x, pos_y, colors)


# ground layer
for j in range(chunk_size):
    for i in range(chunk_size - 1, -1, -1):
        draw_block_iso(i, j, 0, colors_grass)

# tree trunk
tree_i, tree_j = 4, 4
for k in range(1, 3):
    draw_block_iso(tree_i, tree_j, k, colors_wood)

# tree leaves layer around trunk at z=3
leaf_coords = [
    (tree_i, tree_j, 3),
    (tree_i - 1, tree_j, 3),
    (tree_i + 1, tree_j, 3),
    (tree_i, tree_j - 1, 3),
    (tree_i, tree_j + 1, 3)
]
for i, j, k in leaf_coords:
    draw_block_iso(i, j, k, colors_leaves)

print('</svg>')
