import cv2
import glob

passed = 0
error = 0

def driving_on_points(list_points):
    for x in list_points:
    	if img[x[0]][x[1]] == 255:
    	    if x not in visited_point:
                visited_point.append((x[0],x[1]))
                detect_around(x[0],x[1])

def detect_around(i, j):
    list_points = []
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            list_points.append((ii, jj))
    driving_on_points(list_points)

name = glob.glob("pic*.png")
if name:
    for image in name:
        counter = 0
        i = 0
        visited_point = []
        img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        for x in img:
            j = 0
            for y in x:
                if y == 255:
                    if (i, j) not in visited_point:
                        counter += 1
                        visited_point.append((i, j))
                        detect_around(i, j)
                j += 1
            i += 1
        print(f"{image.split('-')[0]} has {image.split('-')[-1][:-4]} shapes , Detected : {counter}")
        if int(image.split("-")[-1][:-4]) == counter:
            print("Pass")
            passed += 1
        else:
            print("Error!!!")
            error += 1
    accuracy = int((passed/len(name))*100)
    print(f"Accuracy : {accuracy}")
    if accuracy != 100:
        print(f"Error Count : {error}")
else:
    print("There is no pics!")
