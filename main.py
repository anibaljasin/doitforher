import cv2



def main():
    doitforher = cv2.imread("doitforher.jpg")
    doitforher_copy = doitforher.copy()
    cat1 = cv2.imread("cat1.jpeg")
    cat2 = cat1.copy()
    cat3 = cat1.copy()
    cat4 = cat1.copy()
    cat5 = cat1.copy()
    cat6 = cat1.copy()
    cat7 = cat1.copy()
    cat8 = cat1.copy()
    cat9 = cat1.copy()
    cat10 = cat1.copy()
    cat11 = cat1.copy()

    print(doitforher_copy.shape)
    print(cat1.shape)

    cat6 = cv2.resize(cat6, (158, 170))
    c1h, c1w, _ = cat6.shape
    top_left = (324, 317)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat6

    cat1 = cv2.resize(cat1, (320, 280))
    c1h, c1w, _ = cat1.shape
    top_left = (384, 428)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat1

    cat2 = cv2.resize(cat2, (250, 190))
    c1h, c1w, _ = cat2.shape
    top_left = (126, 336)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat2

    # Cut slice of image
    c1h, c1w, _ = cat7.shape
    new_width = int(c1w * 0.7)
    cat7 = cat7[:, :new_width]
    cat7 = cv2.resize(cat7, (225, 260))
    c1h, c1w, _ = cat7.shape
    top_left = (735, 192)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat7

    cat3 = cv2.resize(cat3, (160, 110))
    c1h, c1w, _ = cat3.shape
    top_left = (618, 171)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat3


    cat4 = cv2.resize(cat4, (55, 80))
    c1h, c1w, _ = cat4.shape
    top_left = (220, 217)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat4


    cat5 = cv2.resize(cat5, (40, 60))
    c1h, c1w, _ = cat5.shape
    top_left = (285, 200)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat5

    # Cut slice of image
    c1h, c1w, _ = cat8.shape
    new_width = int(c1w * 0.3)
    cat8 = cat8[:, new_width:]
    cat8 = cv2.resize(cat8, (100, 198))
    c1h, c1w, _ = cat8.shape
    top_left = (0, 522)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat8

    # Cut slice of image
    c1h, c1w, _ = cat9.shape
    new_height = int(c1h * 0.5)
    cat9 = cat9[new_height:, :]
    cat9 = cv2.resize(cat9, (240, 110))
    c1h, c1w, _ = cat9.shape
    top_left = (191, 0)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat9

    # Cut slice of image
    c1h, c1w, _ = cat10.shape
    new_height = int(c1h * 0.1)
    cat10 = cat10[-new_height:, :]
    cat10 = cv2.resize(cat10, (180, 30))
    c1h, c1w, _ = cat10.shape
    top_left = (607, 0)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat10

    # Cut slice of image
    c1h, c1w, _ = cat11.shape
    new_height = int(c1h * 0.6)
    new_width = int(c1w * 0.6)
    cat11 = cat11[:new_height, :new_width]
    cat11 = cv2.resize(cat11, (158, 192))
    c1h, c1w, _ = cat11.shape
    top_left = (802, 528)
    doitforher_copy[top_left[1]:top_left[1] + c1h, top_left[0]:top_left[0] + c1w] = cat11



    cv2.imwrite("result.png", doitforher_copy)


if __name__ == "__main__":
    main()
