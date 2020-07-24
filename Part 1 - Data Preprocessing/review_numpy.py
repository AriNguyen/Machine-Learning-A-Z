#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
review numpy array
"""
import numpy as np

data = np.array([1, 2, 3, 4, 5])
dataq = np.array([[1, 2, 3], [3, 3, 3]])
print(dataq.shape[0])
print(dataq.shape[1])
data = data.reshape((data.shape[0], 1))




