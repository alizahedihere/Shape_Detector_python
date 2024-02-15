import cv2
import numpy as np

## specified
w, h, max_shape = 400, 400, 5
n = 20
shapes = ["square", "tirangle", "rectangle", "circle"]
##

def draw_on_img(bw_image, init_dict):
    for x in init_dict:
        if x == "square":
            i, j, t = 0, 0, 35
            for _ in range(init_dict[x]):
                top_left = (np.random.randint(i+2, i+t),
                            np.random.randint(j+2, j+t))
                size = np.random.randint(1, t) 
                bottom_right = (top_left[0] + size, top_left[1] + size)
                cv2.rectangle(bw_image, top_left,
                              bottom_right, (255,255,255), 1)
                i = bottom_right[0]
                j = bottom_right[1]

        elif x == "tirangle":
            i, j, t = 0, 200, 40
            for _ in range(init_dict[x]):
                p1 = (np.random.randint(i+2, i+t), np.random.randint(j+1, j+t))
                p2 = (np.random.randint(i+2, i+t), np.random.randint(j+1, j+t))
                p3 = (np.random.randint(i+2, i+t), np.random.randint(j+1, j+t))
                cv2.line(bw_image, p1, p2, (255,255,255), 1)
                cv2.line(bw_image, p2, p3, (255,255,255), 1)
                cv2.line(bw_image, p3, p1, (255,255,255), 1)
                i = max(p1[0], p2[0], p3[0])
                j = max(p1[1], p2[1], p3[1])

        elif x == "rectangle":
            i, j, t = 200, 200, 28
            for _ in range(init_dict[x]):
                top_left = (np.random.randint(i+2, i+t),np.random.randint(j, j+t))
                size_i = np.random.randint(1, t)
                size_j = np.random.randint(2, t)
                bottom_right = (top_left[0] + size_i, top_left[1] + size_j)
                cv2.rectangle(bw_image, top_left,
                              bottom_right, (255,255,255), 1)
                i = bottom_right[0]
                j = bottom_right[1]
        
        elif x == "circle":
            i, j, t = 200, 0, 20
            for _ in range(init_dict[x]):
                size = np.random.randint(1, t)
                top_left = (np.random.randint(i+1, i+t), np.random.randint(j+size, j+t))
                cv2.circle(bw_image, (top_left[0], top_left[1]), size, (255,255,255), 1)
                i = top_left[0]+(size*2)
                j = top_left[1]+(size*2)

def convert_to_pic(matrix):
    data_array = matrix.astype(np.uint8)
    bw_image = cv2.cvtColor(data_array, cv2.COLOR_GRAY2BGR)
    return bw_image

def create_matrix(w, h):
    matrix = np.zeros((w, h))
    return matrix

# Main
i = 1
for _ in range(n):
    shape_in_pic = 0
    init_dict = {}
    matrix = create_matrix(w, h)
    bw_image = convert_to_pic(matrix)
    for shape in shapes:
        num_shape = np.random.randint(2, max_shape)
        init_dict[shape] = num_shape
        shape_in_pic += num_shape
    draw_on_img(bw_image, init_dict)
    file_name = f"pic{i}-{shape_in_pic}.png"
    cv2.imwrite(file_name,bw_image)
    print(f"{file_name} Created.")
    i += 1
