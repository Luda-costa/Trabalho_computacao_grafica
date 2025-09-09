import cv2
import numpy as np

def imagem():
    img_path = 'fruit1.png'
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(img, 190, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    #kernel = np.ones((5,5),np.uint8)
    kernel = np.array([[1,1,1],
                       [1,0,1],
                       [1,1,1]], np.uint8)
    erosion = cv2.erode(binary, kernel, iterations= 1)
    dilatation = cv2.dilate(erosion, kernel, iterations= 6)

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(erosion)

    print(num_labels)


    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(dilatation)

    print(num_labels)

    img = cv2.imread(img_path)
    for i in range(1, num_labels):

        x, y, w, h, area = stats[i]
        cx, cy = centroids[i]

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(img, (int(cx), int(cy)), 4, (255,0,0), -1)


    cv2.imshow("Imagem resultante", img)
    cv2.imshow("Imagem binario", binary)
    cv2.imshow('Imagem erosao',erosion)
    cv2.imshow('Imagem Dilate', dilatation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

imagem()