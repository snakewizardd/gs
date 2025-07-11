print('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" width="800" height="600" viewBox="0 0 800 600" >')
chunk_size = 8
vec_i_x = 40
vec_i_y = -23.1
vec_j_x = 40
vec_j_y = 23.1
offset_x = 20
offset_y = 200 + 7*23.1
# grass
colors_grass = {'top': '#7cbd6b', 'left': '#5e8c4e', 'right': '#4d7a3d'}
# wood
colors_wood = {'top': '#a0522d', 'left': '#8b4513', 'right': '#6b4513'}
# leaves
colors_leaves = {'top': '#228b22', 'left': '#006400', 'right': '#004b00'}
# function to draw block
def draw_block(pos_x, pos_y, colors):
    print(f'<g transform="translate({pos_x}, {pos_y})">')
    print(f'<path fill="{colors["top"]}" d="M40,46.2 L0,23.1 L40,0 L80,23.1 Z" />')
    print(f'<path fill="{colors["left"]}" d="M0,23.1 L40,46.2 L40,92.4 L0,69.3 Z" />')
    print(f'<path fill="{colors["right"]}" d="M40,46.2 L80,23.1 L80,69.3 L40,92.4 Z" />')
    print('</g>')
# draw base grass
for j in range(chunk_size):
    for i in range(chunk_size -1, -1, -1):
        pos_x = i * vec_i_x + j * vec_j_x + offset_x
        pos_y = i * vec_i_y + j * vec_j_y + offset_y
        draw_block(pos_x, pos_y, colors_grass)
# add tree at i=4, j=4
tree_i = 4
tree_j = 4
# wood at z=1
pos_x = tree_i * vec_i_x + tree_j * vec_j_x + offset_x
pos_y = tree_i * vec_i_y + tree_j * vec_j_y + offset_y - 46.2
draw_block(pos_x, pos_y, colors_wood)
# leaves at z=2
pos_y = pos_y - 46.2
draw_block(pos_x, pos_y, colors_leaves)
# more leaves
# left i-1
pos_x = (tree_i-1) * vec_i_x + tree_j * vec_j_x + offset_x
pos_y = (tree_i-1) * vec_i_y + tree_j * vec_j_y + offset_y - 46.2 *2
draw_block(pos_x, pos_y, colors_leaves)
# right i+1
pos_x = (tree_i+1) * vec_i_x + tree_j * vec_j_x + offset_x
pos_y = (tree_i+1) * vec_i_y + tree_j * vec_j_y + offset_y - 46.2 *2
draw_block(pos_x, pos_y, colors_leaves)
# front j-1
pos_x = tree_i * vec_i_x + (tree_j-1) * vec_j_x + offset_x
pos_y = tree_i * vec_i_y + (tree_j-1) * vec_j_y + offset_y - 46.2 *2
draw_block(pos_x, pos_y, colors_leaves)
# back j+1
pos_x = tree_i * vec_i_x + (tree_j+1) * vec_j_x + offset_x
pos_y = tree_i * vec_i_y + (tree_j+1) * vec_j_y + offset_y - 46.2 *2
draw_block(pos_x, pos_y, colors_leaves)
print('</svg>')