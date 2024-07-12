import cv2
import numpy as np


# 在image中搜索是否包含target，返回按x排序的(x, y)列表
def image_search(image, target):
    # 搜图
    res = cv2.matchTemplate(image, target, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    coords = [coord for coord in zip(*loc[::-1])]

    # 去重
    temp = []
    threshold = 10
    for coord in coords:
        exists = False
        for coord2 in temp:
            if abs(coord[0] - coord2[0]) <= threshold and abs(coord[1] - coord2[1]) <= threshold:
                exists = True
        if not exists:
            temp.append(coord)
    coords = sorted(temp, key=lambda pair: pair[0])
    return coords
