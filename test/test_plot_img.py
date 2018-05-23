# -*- coding: UTF-8 -*-
''' Author: HZT
    Create Date: 20180523
'''
import pytest
from src.plot_img import PlotImg


class TestPlotImg():
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    @pytest.mark.skip(reason="画图会阻塞主线程")
    def test_plot_energe_list(self):
        energe_list = [{'time': 0, 'energe': 1}, {'time': 1, 'energe': 2}]
        PlotImg.plot_energe_list(energe_list)
