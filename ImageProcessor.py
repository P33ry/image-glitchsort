import cv2
import random


def glitchsort(filename: str, outputname: str, lower_canny: int=100, higher_canny: int=200, sorting_length=0, vertical: bool=True):
    """
    Wrapper function for glitchsort_x and glitchsort_y
    :param filename:
    :param outputname:
    :param lower_canny:
    :param higher_canny:
    :param sorting_length:
    :param vertical:
    :return:
    """
    new_img = None
    if vertical:
        new_img = __glitchsort_x(filename, lower_canny, higher_canny, sorting_length)
    else:
        new_img = __glitchsort_y(filename, lower_canny, higher_canny, sorting_length)

    print("Writing output...")
    cv2.imwrite(outputname, new_img)
    print("Done!")


def __glitchsort_x(filename: str, lower_canny: int=100, higher_canny: int=200, sorting_length=0):
    """
    Apply pixel sorting to the given image using canny edge detection to stop sorting.

    Sorting length varies a bit averaging around sorting_length (0 for endless)
    :param filename:
    :param lower_canny:
    :param higher_canny:
    :param sorting_length:
    :return:
    """
    img = cv2.imread(filename)
    width, height, depth = img.shape
    canny = cv2.Canny(img, lower_canny, higher_canny)

    new_img = img.copy()

    print("Sorting...")
    for x in range(width):  # search for first edge
        for y in range(height):
            if canny[x, y] == 255:
                length = int(sorting_length+random.randint(-1, 1)*0.3)

                pixelsort(img, new_img, x, y, dx=0, dy=-1, length=length)
                continue

    return new_img


def __glitchsort_y(filename: str, lower_canny: int=100, higher_canny: int=200, sorting_length=0):
    """
    Apply pixel sorting to the given image using canny edge detection to stop sorting.

    Sorting length varies a bit averaging around sorting_length (0 for endless)
    :param filename:
    :param lower_canny:
    :param higher_canny:
    :param sorting_length:
    :return:
    """
    img = cv2.imread(filename)
    width, height, depth = img.shape
    canny = cv2.Canny(img, lower_canny, higher_canny)

    new_img = img.copy()

    print("Sorting...")
    for y in range(height):  # search for first edge
        for x in range(width):
            if canny[x, y] == 255:
                length = int(sorting_length+random.randint(-1, 1)*0.3)

                pixelsort(img, new_img, x, y, dx=-1, dy=0, length=length)
                continue

    return new_img


def pixelsort(img, new_img, x, y, dx=0, dy=1, length=-1):
    """
    Pixelsort from point (x,y) in direction (dx,dy) for length long (-1 means until end of picture).

    :param img:
    :param new_img:
    :param x:
    :param y:
    :param dx:
    :param dy:
    :return:
    """
    assert(dx != 0 or dy != 0)

    width, height, depth = img.shape

    pixels = []
    todo = length
    while todo is not 0:
        pixels.append([x, y])
        x += dx
        y += dy
        todo -= 1

        if x >= width or x <= 0 or y >= height or y <= 0:  # ran out of bounds
            break


    def get_value(pixel):
        return img[pixel[0], pixel[1], 0]

    sorted_pixels = sorted(pixels, key=get_value)

    for i in range(len(pixels)):
        new_img[pixels[i][0], pixels[i][1]] = img[sorted_pixels[i][0], sorted_pixels[i][1]]
