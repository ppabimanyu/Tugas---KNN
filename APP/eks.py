import numpy as np
import cv2
import math
import pandas as pd
from tqdm import tqdm


def ekstrak(PATH):
    data = []
    for i in tqdm(PATH, desc="load"):
        fileImage = cv2.imread(i)
        img = cv2.cvtColor(fileImage, cv2.COLOR_BGR2GRAY)
        a = cv2.resize(img, (128, 128))
        data.append(a)

    def derajat0(img):
        max = np.max(img)
        imgTmp = np.zeros([max+1, max+1])
        for i in range(len(img)):
            for j in range(len(img[i])-1):
                imgTmp[img[i, j], img[i, j+1]] += 1

        transpos = np.transpose(imgTmp)
        data = imgTmp+transpos

        tmp = 0
        for i in range(len(data)):
            for j in range(len(data)):
                tmp += data[i, j]

        for i in range(len(data)):
            for j in range(len(data)):
                data[i, j] /= tmp

        return data

    def derajat45(img):
        max = np.max(img)
        imgTmp = np.zeros([max+1, max+1])
        for i in range(len(img)-1):
            for j in range(len(img[i])-1):
                imgTmp[img[i+1, j], img[i, j+1]] += 1

        transpos = np.transpose(imgTmp)
        data = imgTmp+transpos

        tmp = 0
        for i in range(len(data)):
            for j in range(len(data)):
                tmp += data[i, j]

        for i in range(len(data)):
            for j in range(len(data)):
                data[i, j] /= tmp

        return data

    def derajat90(img):
        max = np.max(img)
        imgTmp = np.zeros([max+1, max+1])
        for i in range(len(img)-1):
            for j in range(len(img[i])):
                imgTmp[img[i+1, j], img[i, j]] += 1

        transpos = np.transpose(imgTmp)
        data = imgTmp+transpos

        tmp = 0
        for i in range(len(data)):
            for j in range(len(data)):
                tmp += data[i, j]

        for i in range(len(data)):
            for j in range(len(data)):
                data[i, j] /= tmp

        return data

    def derajat135(img):
        max = np.max(img)
        imgTmp = np.zeros([max+1, max+1])
        for i in range(len(img)-1):
            for j in range(len(img[i])-1):
                imgTmp[img[i, j], img[i+1, j+1]] += 1

        transpos = np.transpose(imgTmp)
        data = imgTmp+transpos

        tmp = 0
        for i in range(len(data)):
            for j in range(len(data)):
                tmp += data[i, j]

        for i in range(len(data)):
            for j in range(len(data)):
                data[i, j] /= tmp

        return data

    hasil = []
    for i in tqdm(range(len(data)), desc='GLCM'):
        dat = [derajat0(data[i]), derajat45(data[i]),
               derajat90(data[i]), derajat135(data[i])]
        hasil.append(dat)

    def contras(data):
        contras = 0
        for i in range(len(data)):
            for j in range(len(data)):
                contras += data[i, j]*pow(i-j, 2)
        return contras

    def entropy(data):
        entro = 0
        for i in range(len(data)):
            for j in range(len(data)):
                if data[i, j] > 0.0:
                    entro += -(data[i, j] * math.log(data[i, j]))
        return entro

    def homogentitas(data):
        homogen = 0
        for i in range(len(data)):
            for j in range(len(data)):
                homogen += data[i, j]*(1+(pow(i-j, 2)))
        return homogen

    def energy(data):
        ener = 0
        for i in range(len(data)):
            for j in range(len(data)):
                ener += data[i, j]**2
        return ener

    future = []
    for j in tqdm(range(len(hasil)), desc='Ekstraksi'):
        da = []
        da.append(PATH[j])
        for i in hasil[j]:
            da.append(energy(i))
            da.append(homogentitas(i))
            da.append(entropy(i))
            da.append(contras(i))
        da.append(str(PATH[j].split("/")[2]))
        future.append(da)

    tabel = ['file', 'energy_0', 'homogenity_0', 'entrophy_0', 'contras_0', 'energy_45', 'homogenity_45', 'entrophy_45', 'contras_45',
             'energy_90', 'homogenity_90', 'entrophy_90', 'contras_90', 'energy_135', 'homogenity_135', 'entrophy_135', 'contras_135', 'Target']
    df = pd.DataFrame(future, columns=tabel)

    return df
