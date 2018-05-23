# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180523
'''
import matplotlib.pyplot as plt


class PlotImg():
    def __init__(self):
        pass

    @staticmethod
    def plot_energe_list(energe_list):
        if not energe_list:
            raise ValueError
        x = []
        y = []
        y_max = 0
        for point in energe_list:
            x.append(point['time'])
            y.append(point['energe'])
            if point['energe'] > y_max:
                y_max = point['energe']
        plt.bar(x, y, width=0.3, facecolor='black', edgecolor='white')
        plt.ylim(0, y_max)
        plt.show()
