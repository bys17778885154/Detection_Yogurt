# -*- coding: utf-8 -*-
"""
运行本项目需要安装的库：
    opencv-contrib-python 4.5.1.48
    PyQt5 5.15.2
    scikit-learn 0.22
    numba 0.53.0
    imutils 0.5.4
    filterpy 1.4.5

点击运行主程序runMain.py，程序所在文件夹路径中请勿出现中文
"""
# -*- coding: utf-8 -*-
# 本程序用于多目标检测追踪
# @Time    : 2021/4/30 17:00
# @Author  : Yogurt
# @Software: PyCharm
import os
import warnings

from DetectionTracking import Ui_MainWindow
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 不同值设置的是基础log信息（base_logging），运行时会输出base等级及其之上（更为严重）的信息
    # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "0"  # INFO（通知）
    # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"  # WARNING（警告）
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # ERROR（错误）
    # os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # FATAL（致命的）

    warnings.filterwarnings(action='ignore')  # 警告过滤器

    app = QApplication(argv)  # 实例化一个应用对象

    window = QMainWindow()  # 窗口界面的基本控件，它提供了基本的应用构造器。默认情况下，构造器是没有父级的，没有父级的构造器被称为窗口(window)。

    ui = Ui_MainWindow(window)  # 加载ui自定义控件，在此处添加用户代码

    window.show()  # 让控件在桌面上显示出来。

    exit(app.exec_())  # 确保主循环安全退出
