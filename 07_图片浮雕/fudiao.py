import cv2
import numpy as np
import time

img = cv2.imread('./liuqun.png')
img = np.array(img)
img = img / 255.0


a = time.time()
size = 3
step = 1

kernel = [[1, 1, 1],
          [1, -7, 1],
          [1, 1, 1]]
kernel = np.array(kernel)

is_first = 1
result = []

for i in range(img.shape[2]):
    result_channel = []
    for j in range(0, img.shape[0], step):
        temp = []
        for k in range(0, img.shape[1], step):
            # print(img.shape, i, j, k)
            if j == 0 and k == 0:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[1, 2] * img[j, k + 1, i] + kernel[2, 1] * img[
                    j + 1, k, i] + kernel[2, 2] * img[j + 1, k + 1, i]
                temp.append(temp_r)
            elif j == 0 and k != 0 and k != img.shape[1] - 1:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[1, 2] * img[j, k + 1, i] + kernel[2, 1] * img[
                    j + 1, k, i] + kernel[2, 2] * img[j + 1, k + 1, i] + kernel[1, 0] * img[j, k - 1, i] + kernel[
                             2, 0] * img[j + 1, k - 1, i]
                temp.append(temp_r)
            elif j != 0 and k == 0 and j != img.shape[0] - 1:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[1, 2] * img[j, k + 1, i] + kernel[2, 1] * img[
                    j + 1, k, i] + kernel[2, 2] * img[j + 1, k + 1, i] + kernel[0, 1] * img[j - 1, k, i] + kernel[
                             0, 2] * img[j - 1, k + 1, i]
                temp.append(temp_r)
            elif j == img.shape[0] - 1 and k == img.shape[1] - 1:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[0, 0] * img[j - 1, k - 1, i] + kernel[0, 1] * img[
                    j - 1, k, i] + kernel[1, 0] * img[j, k - 1, i]
                temp.append(temp_r)
            elif j == img.shape[0] - 1 and k != img.shape[1] - 1 and k != 0:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[0, 0] * img[j - 1, k - 1, i] + kernel[0, 1] * img[
                    j - 1, k, i] + kernel[1, 0] * img[j, k - 1, i] + kernel[1, 2] * img[j, k + 1, i] + kernel[0, 2] * \
                         img[j - 1, k + 1, i]
                temp.append(temp_r)
            elif j != img.shape[0] - 1 and k == img.shape[1] - 1 and j != 0:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[0, 0] * img[j - 1, k - 1, i] + kernel[0, 1] * img[
                    j - 1, k, i] + kernel[1, 0] * img[j, k - 1, i] + kernel[2, 1] * img[j + 1, k, i] + kernel[2, 0] * \
                         img[j + 1, k - 1, i]
                temp.append(temp_r)
            elif j == img.shape[0] - 1 and k == 0:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[0, 1] * img[j - 1, k, i] + kernel[1, 2] * img[
                    j, k + 1, i] + kernel[0, 2] * img[j, k, i]
                temp.append(temp_r)
            elif j == 0 and k == img.shape[1] - 1:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[2, 1] * img[j + 1, k, i] + kernel[1, 0] * img[
                    j, k - 1, i] + kernel[2, 0] * img[j + 1, k - 1, i]
                temp.append(temp_r)
            else:
                temp_r = kernel[1, 1] * img[j, k, i] + kernel[1, 2] * img[j, k + 1, i] + kernel[2, 1] * img[
                    j + 1, k, i] + kernel[2, 2] * img[j + 1, k + 1, i] + kernel[1, 0] * img[j, k - 1, i] + kernel[
                             2, 0] * img[j + 1, k - 1, i] + kernel[0, 1] * img[j - 1, k, i] + kernel[
                             0, 2] * img[j - 1, k + 1, i] + kernel[0, 0] * img[j - 1, k - 1, i]
                temp.append(temp_r)
        result_channel.append(temp)
    if is_first == 1:
        is_first = 0
        result = np.expand_dims(np.array(result_channel),axis=-1)
    else:
        result = np.concatenate((result,np.expand_dims(np.array(result_channel),axis=-1)),axis=2)
b = time.time()
result = np.array(result)
cv2.imwrite('./result.jpg', result * 255.0)
print(b-a)
