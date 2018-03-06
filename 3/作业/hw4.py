import cv2
def LapLace(file1, file2, masking, roiX, roiY):
    img1 = cv2.imread(file1)
    img2 = cv2.imread(file2)
    img_mask = cv2.imread(masking)
    # 获得图像的尺寸元组。元组有三个属性，长，宽，深度
    shape1 = img1.shape
    shape2 = img2.shape
    # 统一图片大小，将其设置为2的倍数
    # 因为我们需要五层金字塔，所以需要的大小为2^5=32
    #这样可以避免add和subtract操作报错
    img1 = cv2.resize(img1, dsize=(int(shape1[1]/32)*32, int(shape1[0]/32)*32))
    img2 = cv2.resize(img2, dsize=(int(shape2[1]/32)*32, int(shape2[0]/32)*32))
    #构筑img1的高斯金字塔并输出
    copy = img1.copy()
    gpa = [copy]
    for i in range(6):
        copy = cv2.pyrDown(copy)
        gpa.append(copy)
        cv2.imwrite(file1+"gausstower%d.jpg"%i, copy)
    # 构筑img2的高斯金字塔并输出
    copy = img2.copy()
    gpb = [copy]
    for i in range(6):
        copy = cv2.pyrDown(copy)
        gpb.append(copy)
        cv2.imwrite(file2+"gausstower%d.jpg"%i, copy)
    # 构筑img1的拉普拉斯金字塔
    lpa = [gpa[5]]
    for i in range(5, 0, -1):
        size = (gpa[i - 1].shape[1], gpa[i - 1].shape[0])
        GE = cv2.pyrUp(gpa[i], dstsize = size)
        L = cv2.subtract(gpa[i - 1], GE)
        lpa.append(L)
        cv2.imwrite(file1+"laplacetower%d.jpg"%i, L)
    # 构筑img2的拉普拉斯金字塔
    lpb = [gpb[5]]
    for i in range(5, 0, -1):
        size = (gpb[i - 1].shape[1], gpb[i - 1].shape[0])
        GE = cv2.pyrUp(gpb[i], dstsize = size)
        L = cv2.subtract(gpb[i - 1], GE)
        lpb.append(L)
        cv2.imwrite(file2+"laplacetower%d.jpg"%i, L)
    # 重建img1
    # 将金字塔各层叠加
    re1 = lpa[0]
    for i in range(1, 6):
        re1 = cv2.pyrUp(re1)
        re1 = cv2.add(re1, lpa[i])
    # 重建img2
    # 将金字塔各层叠加
    re2 = lpb[0]
    for i in range(1, 6):
        re2 = cv2.pyrUp(re2)
        re2 = cv2.add(re2, lpb[i])
    # 恢复图像的大小
    img1 = cv2.resize(re1, dsize=(shape1[1], shape1[0]))
    img2 = cv2.resize(re2, dsize=(shape2[1], shape2[0]))
    # 融合结果图像的初始值设为被融合图像，然后遍历需要融合的部分
    height = min(roiX + img2.shape[0], img1.shape[0])
    width = min(roiY + img2.shape[1], img1.shape[1])
    img2 = img2[0:height - roiX, 0:width - roiY]
    img_mix = img1
    for i in range(roiX, height):
        for j in range(roiY, width):
            if img_mask[i - roiX][j - roiY].all() != 0:
                img_mix[i][j] = img1[i][j] * 0.5 + img2[i - roiX][j - roiY] * 0.5
    return img_mix
# 全局 同时处理三个图像
pyramid1 = LapLace("1-1.jpg", "1-2.jpg", "1-masking.jpg", 6, 22)
cv2.imwrite("pyramid1.jpg", pyramid1)
pyramid2 = LapLace("2-1.jpg", "2-2.jpg", "2-masking.jpg", 236, 31)
cv2.imwrite("pyramid2.jpg", pyramid2)
pyramid3 = LapLace("3-1.jpg", "3-2.jpg", "3-masking.jpg", 206, 208)
cv2.imwrite("pyramid3.jpg", pyramid3)

