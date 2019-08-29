# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from agent import *
import time
import pandas as pd


class Ui_Form(object):

    def setupUi(self, Form, user_name, w, i):

        # 1. 初始化主体
        self.user_name = user_name
        self.i = str(i)
        self.env = Environment(16, 4, 1-float(w))  # 环境
        self.robot = Robot(4) # 机器人
        self.dic_state_geo = {}
        geos = [(x, y, 50, 50) for y in [230, 290, 350, 410] for x in [60, 120, 180, 240]]
        states = [x for x in range(16)]
        for state, geo in zip(states, geos):
            self.dic_state_geo[state] = geo
        self.task_count = [0]
        self.robot_task_count = [0]
        self.time = [time.time()]
        self.h_action = [None]
        self.step = 0


        # 2. UI元素
        Form.setObjectName("Form")
        Form.resize(701, 569)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(490, 310, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(64)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 240, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 224, 224);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 320, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 224, 224);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 400, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 224, 224);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 320, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"background-color: rgb(224, 224, 224);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(55, 215, 240, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(55, 275, 240, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(55, 335, 240, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(55, 395, 240, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(55, 455, 240, 21))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(55, 225, 3, 240))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(115, 225, 3, 240))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(175, 225, 3, 240))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(235, 225, 3, 240))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(295, 225, 3, 240))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 230, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 410, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 301, 50, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 20, 621, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 80, 621, 101))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 190, 621, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(120, 290, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(180, 350, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(50, 490, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(50, 520, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(260, 490, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(260, 520, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Human Robot Game"))
        self.label.setText(_translate("Form", '%02d' % self.step))
        self.pushButton.setText(_translate("Form", "⬆️"))
        self.pushButton.clicked.connect(lambda: self.move(h_action=0))
        self.pushButton_2.setText(_translate("Form", "➡️"))
        self.pushButton_2.clicked.connect(lambda: self.move(h_action=1))
        self.pushButton_3.setText(_translate("Form", "⬇️"))
        self.pushButton_3.clicked.connect(lambda: self.move(h_action=2))
        self.pushButton_4.setText(_translate("Form", "⬅️"))
        self.pushButton_4.clicked.connect(lambda: self.move(h_action=3))
        self.label_2.setText(_translate("Form", "①"))
        self.label_3.setText(_translate("Form", "②"))
        self.label_4.setText(_translate("Form", "steps"))
        self.label_5.setText(_translate("Form", "首先，感谢您对本研究的大力支持！"))
        self.label_6.setText(_translate("Form", "请看左下方的游戏场地图。\"人\"表示您，\"机\"表示机器人，\"①\"和\"②\"表示两个任务（\"①\"和\"②\"位置固定不变，且优先级相同。）"
                                                "您与机器人每次同时移动一步，当你们同时到达\"①\"或\"②\"时，共同完成任务数字加1。随即\"人\"与\"机\"位置随机初始化，下轮游戏开始。"
                                                "屏幕下方展示了\"机\"到达任务的数量，和你们二者同时到达任务场地的数量。"))
        self.label_7.setText(_translate("Form", "现在已经为您初始化好了第一轮的位置，点击右侧操作按钮即可开始实验。再次感谢您的支持！"))
        self.label_8.setText(_translate("Form", "H"))
        self.label_9.setText(_translate("Form", "R"))
        self.label_10.setText(_translate("Form", "完成任务数："))
        self.label_11.setText(_translate("Form", "机："))
        self.label_12.setText(_translate("Form", str(sum(self.task_count))))
        self.label_13.setText(_translate("Form", str(sum(self.robot_task_count))))

    #
    def move(self, h_action):
        self.label_null()
        # 动作记录
        if self.env.human_state in [0, 1, 2 ,3] and h_action == 0 or \
                self.env.human_state in [0, 4, 8, 12] and h_action == 3 or \
                self.env.human_state in [3, 7, 11, 15] and h_action == 1 or \
                self.env.human_state in [12, 13, 14, 15] and h_action == 2:
            print(self.step)
            h_action == None
        self.h_action.append(h_action if h_action else np.nan)
        # 位置更新
        if self.i in '012':
            r_action = self.robot.ql(16, self.env.robot_state, self.env.reward_matrix, self.env.switch_matrix)
        else:
            r_action = self.robot.pi_iter(16, self.env.robot_state, self.env.reward_matrix, self.env.switch_matrix)
        self.env.state_update(h_action, r_action)
        self.env.reward_matrix_update(0.5)
        # 位置展示
        self.label_9.setText("R")  # 恢复R的标志
        if self.env.robot_state == self.env.human_state:
            self.label_9.setText("HR")
        self.label_8.setGeometry(QtCore.QRect(*self.dic_state_geo[self.env.human_state]))
        self.label_9.setGeometry(QtCore.QRect(*self.dic_state_geo[self.env.robot_state]))
        # 任务完成效果更新
        if self.env.task_completed():
            self.robot_task_count.append(1)
            self.task_count.append(1)
            self.env.state_refresh(16)
            self.label_ok()
            self.label_9.setText("R")  # 恢复R的标志
            self.label_8.setGeometry(QtCore.QRect(*self.dic_state_geo[self.env.human_state]))
            self.label_9.setGeometry(QtCore.QRect(*self.dic_state_geo[self.env.robot_state]))
        else:
            if self.env.robot_state == self.env.task1_state or self.env.robot_state == self.env.task2_state:
                self.robot_task_count.append(1)
            else:
                self.robot_task_count.append(0)
            self.task_count.append(0)
        # 任务完成效果展示
        self.label_12.setText(str(sum(self.task_count)))
        self.label_13.setText(str(sum(self.robot_task_count)))
        # 时间戳记录
        self.time.append(time.time())
        # 步数更新
        self.step += 1
        # 步数判断
        self.label.setText('%02d' % self.step)
        # 结束条件
        if self.step == 99:
            # 按钮失灵
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_4.setEnabled(False)
            # 提示语句
            self.label_5.setText("")
            font = QtGui.QFont()
            font.setPointSize(20)
            self.label_6.setFont(font)
            self.label_6.setAlignment(QtCore.Qt.AlignCenter)
            self.label_6.setText("实验结束！感谢您的配合！请点击左上角退出程序。")
            self.label_7.setText("")
            # 存储实验结果
            result = pd.Series(range(100)).to_frame()
            result.columns = ['step']
            result['robot_task_count'] = self.robot_task_count
            result['task_count'] = self.task_count
            result['timestamp'] = self.time
            result['h_action'] = self.h_action
            result.to_csv('result/'+self.user_name+'_'+self.i+'.csv', index=None)

    def label_ok(self):
        self.label_5.setText("")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setText("Task Completed! \n下一轮开始!")
        self.label_7.setText("")

    def label_null(self):
        self.label_5.setText("")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setText("--------")
        self.label_7.setText("")