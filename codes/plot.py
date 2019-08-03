import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

t, x, y = np.genfromtxt('test3', comments='#', skip_header=1, delimiter=',', unpack=True)
pd.read_csv('test3', skiprows=1, header=None)

f = open('test3', 'r+')
read_data = f.read()
f.close()
