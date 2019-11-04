# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import psutil
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    # upload  download  share delete  newfile  searchfile selectfile  refresh back  forward
    # 点击树菜单触发
    def treeclick(self, index):
        item = self.treeWidget.currentItem()
        i = '{0}{1}'.format(item.text(0)[0:1], ':')
        self.getFile(i)
    def upload(self,index):
        print("上传被点击")
    def download(self,index):
        print("下载被点击")
    def share(self,index):
        print("分享被点击")
    def delete(self,index):
        print("上传被点击")
    def newfile(self,index):
        print("新建被点击")
    def selectfile(self,index):
        print("选中被点击")
    def searchfile(self,index):
        print("查询被点击")
    def refresh(self,index):
        print("刷新被点击")
    def back(self,index):
        print("后退被点击")
    def forward(self,index):
        print("前进被点击")
    def getFile(self,path):
        marginLeft = 10
        marginRight = 10
        width = 121
        height = 101
        print(path)
        testList=os.listdir(path)
        _translate = QtCore.QCoreApplication.translate
        self.scrollAreaWidgetContents=None
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setMinimumSize(250, 2000)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        for index, value in enumerate(testList):
            print(testList)
            if index!=0 and index % 6 == 0:
                marginRight = marginRight + 100
                marginLeft = 10
            if index % 6 == 0:
                marginLeft = 10
            else:
                marginLeft = marginLeft + 120
            i = '{0}-{1}-{2}-{3}'.format(marginLeft, marginRight, width, height)
            print('位置', i)
            name = '{0}{1}'.format('frame_file',index)
            pushButtonName ='{0}{1}'.format('pushButton_file',index)
            verticalLayoutWidget='{0}{1}'.format('verticalLayoutWidget_file',index)
            verticalLayout='{0}{1}'.format('verticalLayout_file',index)
            label='{0}{1}'.format('label_file',index)

            setattr(self, name, QtWidgets.QFrame(self.scrollAreaWidgetContents))
            getattr(self, name).setGeometry(QtCore.QRect(marginLeft, marginRight, width, height))
            getattr(self, name).setFrameShape(QtWidgets.QFrame.StyledPanel)
            getattr(self, name).setFrameShadow(QtWidgets.QFrame.Raised)
            getattr(self, name).setObjectName(name)

            setattr(self, pushButtonName, QtWidgets.QPushButton(getattr(self, name)))
            getattr(self, pushButtonName).setGeometry(QtCore.QRect(20, 0, 81, 61))
            getattr(self, pushButtonName).setLayoutDirection(QtCore.Qt.LeftToRight)
            getattr(self, pushButtonName).setText("")

            icon11 = QtGui.QIcon()
            icon11.addPixmap(QtGui.QPixmap("../ioc/文件夹.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
            getattr(self, pushButtonName).setIcon(icon11)
            getattr(self, pushButtonName).setIconSize(QtCore.QSize(64, 64))
            getattr(self, pushButtonName).setObjectName(pushButtonName)
            getattr(self, pushButtonName).pressed.connect(self.selectfile)
            setattr(self, verticalLayoutWidget, QtWidgets.QWidget(getattr(self, name)))
            getattr(self, verticalLayoutWidget).setGeometry(QtCore.QRect(0, 60, 121, 41))
            getattr(self, verticalLayoutWidget).setObjectName(verticalLayoutWidget)

            setattr(self, verticalLayout, QtWidgets.QVBoxLayout(getattr(self, verticalLayoutWidget)))
            getattr(self, verticalLayout).setContentsMargins(0, 0, 0, 0)
            getattr(self, verticalLayout).setObjectName(verticalLayout)

            setattr(self, label, QtWidgets.QLabel(getattr(self, verticalLayoutWidget)))
            getattr(self, label).setAlignment(QtCore.Qt.AlignCenter)
            getattr(self, label).setObjectName(label)
            getattr(self, label).setText(_translate("MainWindow", value))
            getattr(self, verticalLayout).addWidget(getattr(self, label))
            print("我走完了")

    def setupUi(self, MainWindow):
        #数据模型
        self.model = QtWidgets.QDirModel()
        MainWindow.setObjectName("家庭数据中心")
        MainWindow.resize(943, 568)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 161, 531))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(10, 0, 151, 481))
        # 给树绑定事件
        self.treeWidget.clicked.connect(self.treeclick)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/电脑.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        list = psutil.disk_partitions()
        # 实例化磁盘的个数
        for index in list:
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
         #实例化数据结束
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ioc/文档.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../ioc/删除.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon2)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 493, 151, 16))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(190, 40, 741, 41))
        self.frame_2.setAutoFillBackground(True)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 414, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../ioc/上传.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../ioc/下载.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../ioc/分享.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../ioc/网盘-新建文件夹.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(190, 80, 741, 41))
        self.frame_3.setAutoFillBackground(True)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_3)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 161, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_8.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../ioc/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../ioc/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../ioc/刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 10, 169, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_9.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../ioc/搜索.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon10)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(190, 130, 741, 411))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")


        # 计算位置
        self.marginLeft = 10
        self.marginRight = 10
        self.width = 121
        self.height = 101
        path = '{0}{1}'.format('C', ':')
        self.getFile(path)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(self.upload)
        self.pushButton.clicked.connect(self.download)
        self.pushButton_4.clicked.connect(self.share)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.newfile)
        self.pushButton_9.clicked.connect(self.searchfile)
        self.pushButton_8.clicked.connect(self.forward)
        self.pushButton_7.clicked.connect(self.back)
        self.pushButton_6.clicked.connect(self.refresh)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "我的电脑"))
        list = psutil.disk_partitions()
        for index, value in enumerate(list):
            self.treeWidget.topLevelItem(0).child(index).setText(0, _translate("MainWindow", value.device[0:1] + "盘"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "数据中心"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "图片"))
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "视频"))
        self.treeWidget.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "音乐"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "回收站"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "上传"))
        self.pushButton.setText(_translate("MainWindow", "下载"))
        self.pushButton_4.setText(_translate("MainWindow", "分享"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))
        self.pushButton_5.setText(_translate("MainWindow", "新建文件夹"))
        self.pushButton_6.setText(_translate("MainWindow", "刷新"))
        # for attr in dir(self):
        #     if not attr.startswith('__') and 'label_file' in attr:
        #          getattr(self, attr).setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())