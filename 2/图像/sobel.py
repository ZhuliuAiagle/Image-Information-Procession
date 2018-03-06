# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:35:18 2017

@author: 逐流
"""

import numpy as np
import cv2
# Load an color image in grayscale
img = cv2.imread('flower.jpg',0)
cv2.imshow('image',img)