# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import psutil
import os
import stat
import sip
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from longer.QDoublePushButton import QDoublePushButton
from longer.fileSearchThread import fileSearchThread

class Ui_MainWindow(object):
    # upload  download  share delete  newfile  searchfile selectfile  refresh back  forward
    # 点击树菜单触发
    def treeclick(self, index):
        self.pushButton_7.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/rightnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        self.pushButton_8.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/leftnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)

        self.nextPath=""
        self.clickSelectList=[]

        _translate = QtCore.QCoreApplication.translate
        item = self.treeWidget.currentItem()
        i = '{0}{1}'.format(item.text(0)[0:1], ':')
        if '盘' in item.text(0):
            self.label_2.setText(_translate("MainWindow", i))
            self.getFile( os.listdir(i))
        else:
            self.label_2.setText(_translate("MainWindow", item.text(0)))
     #滚动置顶
    def goTop(self):
        self.scrollBar = self.scrollArea.verticalScrollBar()
        self.scrollBar.setValue(0)
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
    def selectfile(self):
        print("选中被点击")
    def searchfile(self,index):
        print("查询被点击")
        Ui_MainWindow.result=[]
        self.ButtonClicked(self.lineEdit.text())
        print("搜索结果",self.result)

    #搜索
    def ButtonClicked(self,text):
        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        keyword = text
        self.result=[]
        path = self.label_2.text()
        if ':/' in path:
            path = path.replace(":/", ":\\\\")
            path = '{0}{1}'.format(path, "\\")
        else:
            path = path.replace(":", ":\\\\")
        print("最终的查询路径",path)
        self.thread=fileSearchThread(keyword,path)
        self.thread.sinOut.connect(self.slotAdd)
        self.thread.start()

    #搜索用的
    def slotAdd(self,filename):
        self.result.append(str(filename))
        self.getFile(self.result)
        print(self.result)
    def refresh(self,index):
        self.goTop()
        text = self.label_2.text()
        try:
            self.getFile(os.listdir(text))
        except PermissionError as e:  # 发生异常执行这块代码
            self.label_2.setText(_translate("MainWindow", text))
            QMessageBox.warning(self.centralwidget, "错误提示", "系统拒绝访问！", QMessageBox.Yes)
        print("刷新被点击")

    def back(self,index):
        _translate = QtCore.QCoreApplication.translate
        text = self.label_2.text()
        # 为返回做准备
        self.nextPath = text
        self.pushButton_7.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/rightcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        #返回结束
        i=self.Index(text,'/')
        self.label_2.setText(_translate("MainWindow", text[0:i]))
        try:
            self.getFile(os.listdir(text[0:i]))
        except PermissionError as e:  # 发生异常执行这块代码
            self.label_2.setText(_translate("MainWindow", text))
            QMessageBox.warning(self.centralwidget, "错误提示", "系统拒绝访问！", QMessageBox.Yes)
        if not '/' in text[0:i]:
            self.pushButton_8.setEnabled(False)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("../ioc/leftnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.pushButton_8.setIcon(icon1)


    def forward(self,index):
        self.clickSelectList = []
        #下一步设计
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("MainWindow", self.nextPath))
        try:
            self.getFile(os.listdir(self.nextPath))
        except PermissionError as e:  # 发生异常执行这块代码
            self.label_2.setText(_translate("MainWindow", text))
            QMessageBox.warning(self.centralwidget, "错误提示", "系统拒绝访问！", QMessageBox.Yes)
        self.label_2.setText(_translate("MainWindow", self.nextPath))
        self.nextPath = ''
        self.pushButton_7.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/rightnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon)
        #放回按钮的可点击
        self.pushButton_8.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../ioc/leftcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon1)
        print("前进被点击")
    #查找角标最后一次出现的位置
    def Index(self,str1, c):
        icount = 0
        for index, ch in enumerate(str1):
            if ch == c:
                icount =index
        return icount
    def doDoubleClick(self,index,value):
        self.clickSelectList = []
        #后退按钮为true,可点击
        self.pushButton_8.setEnabled(True)
        icon= QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ioc/leftcan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon)
        _translate = QtCore.QCoreApplication.translate
        text = self.label_2.text()
        item = self.treeWidget.currentItem()
        i = '{0}{1}{2}'.format(text, '/', value)
        if os.path.isdir(i):
            self.label_2.setText(_translate("MainWindow", i))
            try:
                self.getFile(os.listdir(i))
            except PermissionError as e:  #发生异常执行这块代码
                self.label_2.setText(_translate("MainWindow", text))
                QMessageBox.warning(self.centralwidget,"错误提示","系统拒绝访问！",QMessageBox.Yes)

    def remember(self,index,value):
        _translate = QtCore.QCoreApplication.translate
        text = self.label_2.text()
        item = self.treeWidget.currentItem()
        name='{0}{1}'.format('pushButton_file',index)
        labelname = '{0}{1}'.format('label_file', index)
        getattr(self, name).setStyleSheet("background-color: rgb(255, 255, 255);")
        if ':' in getattr(self, labelname).text():
            url=getattr(self, labelname).text()
            url=url.replace(':\\\\',':\\')
            self.clickSelectList.append(url)
        else:
            url='{0}{1}{2}'.format(text,"\\",getattr(self, labelname).text())
            url = url.replace('/','\\')
            self.clickSelectList.append(url)
        print(self.clickSelectList)

    def getFile(self,testList):
        marginLeft = 0
        marginRight = 0
        width = 1
        height = 1
        layoutWidgetHeight=92
        _translate = QtCore.QCoreApplication.translate
        for attr in dir(self):
            if not attr.startswith('__') and 'frame_file' in attr:
                for i in range(self.gridLayout.count()):
                    self.gridLayout.itemAt(i).widget().deleteLater()
        for index, value in enumerate(testList):
            if index == 0 and marginLeft==0 and marginRight==0:
                marginRight = 0
                marginLeft = marginLeft + 1
                layoutWidgetHeight = 92 + layoutWidgetHeight
            elif index!=0 and index % 6 == 0:
                marginRight =0
                marginLeft =marginLeft + 1
                layoutWidgetHeight = 92 + layoutWidgetHeight
            else:
                marginRight = marginRight + 1
            i = '{0}-{1}-{2}-{3}'.format(marginLeft, marginRight, width, height)
            print('位置', i)
            name = '{0}{1}'.format('frame_file',index)

            layoutWidget ='{0}{1}'.format('layoutWidget_file',index)
            verticalLayoutWidget='{0}{1}'.format('verticalLayoutWidget_file',index)
            verticalLayout='{0}{1}'.format('verticalLayout_file',index)
            label='{0}{1}'.format('label_file',index)
            pushButton='{0}{1}'.format('pushButton_file',index)
            setattr(self, name, QtWidgets.QFrame(self.gridLayoutWidget))
            getattr(self, name).setFrameShape(QtWidgets.QFrame.StyledPanel)
            getattr(self, name).setFrameShadow(QtWidgets.QFrame.Raised)
            getattr(self, name).setObjectName(name)

            setattr(self, layoutWidget, QtWidgets.QWidget(getattr(self, name)))
            getattr(self, layoutWidget).setGeometry(QtCore.QRect(20, 10, 78, 92))
            getattr(self, layoutWidget).setObjectName(layoutWidget)

            setattr(self, verticalLayout, QtWidgets.QVBoxLayout(getattr(self, layoutWidget)))
            getattr(self, verticalLayout).setContentsMargins(0, 0, 0, 0)
            getattr(self, verticalLayout).setObjectName(verticalLayout)

            setattr(self, pushButton, QDoublePushButton("aaaa",getattr(self, layoutWidget)))
            getattr(self, pushButton).setLayoutDirection(QtCore.Qt.LeftToRight)
            getattr(self, pushButton).setStyleSheet("border:none;")
            getattr(self, pushButton).setText("")
            icon11 = QtGui.QIcon()
            if not '.' in value:
               icon11.addPixmap(QtGui.QPixmap("../ioc/文件夹.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #BMP、JPG、JPEG、PNG、GIF,ico
            elif '.png' in value  or  '.bmp' in value  or'.gif' in value or '.ico'  in value or '.jpg' in value or '.jpge' in value:
               icon11.addPixmap(QtGui.QPixmap("../ioc/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #音频.mp3.wma
            elif '.mp3' in value or '.wma' in value:
                icon11.addPixmap(QtGui.QPixmap("../ioc/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # .doc”和“.docx
            elif '.docx' in value or '.doc' in value:
                 icon11.addPixmap(QtGui.QPixmap("../ioc/word.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            # 程序
            elif '.exe' in value or '.sys' in value or '.com' in value:
                 icon11.addPixmap(QtGui.QPixmap("../ioc/应用.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            #视频avi,mpg,mpeg,rm,rmvb,dat（VCD中使用）,wmv,mov
            elif '.avi' in value or '.mpg' in value or '.mpeg' in value or '.rm' in value or '.rmvb' in value or '.dat' in value or '.wmv' in value or '.mov' in value or '.mp4' in value:
                icon11.addPixmap(QtGui.QPixmap("../ioc/img.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                icon11.addPixmap(QtGui.QPixmap("../ioc/other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            getattr(self, pushButton).setIcon(icon11)
            getattr(self, pushButton).setIconSize(QtCore.QSize(64, 64))
            getattr(self, pushButton).setObjectName(pushButton)
            getattr(self, pushButton).setCheckable(True)
            # 给绑定事件 partial(self.remember)
            getattr(self, pushButton).clicked.connect(partial(self.remember,index,value))
            getattr(self, pushButton).doubleClicked.connect(partial(self.doDoubleClick,index,value))
            getattr(self, pushButton)
            getattr(self, verticalLayout).addWidget( getattr(self, pushButton))
            setattr(self, label, QtWidgets.QLabel(getattr(self, layoutWidget)))
            getattr(self, label).setAlignment(QtCore.Qt.AlignCenter)
            getattr(self, label).setObjectName(label)
            getattr(self, verticalLayout).addWidget(getattr(self, label))
            getattr(self, label).setObjectName(label)
            getattr(self, label).setText(_translate("MainWindow", value))
            self.gridLayout.addWidget(getattr(self, name), marginLeft,marginRight, 1, 1)
            if index == len(testList) - 1 and index < 6:
                self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 78*(index+1+1), layoutWidgetHeight))
            else:
                if layoutWidgetHeight>2000:
                    self.scrollAreaWidgetContents.setMinimumSize(250, layoutWidgetHeight+1000)
                    self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, layoutWidgetHeight+1000))
                else:
                    self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 721, layoutWidgetHeight))
            self.goTop()


    def setupUi(self, MainWindow):
        #数据模型
        self.model = QtWidgets.QDirModel()
        MainWindow.setObjectName("家庭数据中心")
        MainWindow.resize(950, 568)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10,40, 161, 531))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.treeWidget = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget.setGeometry(QtCore.QRect(10, 0, 151, 461))
        _translate = QtCore.QCoreApplication.translate
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", ""))
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
        self.treeWidget.expandAll()
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 483, 151, 16))
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
        icon7.addPixmap(QtGui.QPixmap("../ioc/leftnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_2.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_7.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../ioc/rightnot.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setObjectName("pushButton_7")
        #设置禁用
        self.pushButton_7.setEnabled(False)
        self.pushButton_8.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../ioc/刷新.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon9)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(560,6 , 169, 26))
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
        #路径保存的地方
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(190, 5, 351, 20))
        self.label_2.setFont(QtGui.QFont("Roman times",12,QtGui.QFont.Bold))

        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(190, 130, 741, 411))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setMinimumSize(250, 2000)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 739, 409))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 721, 600))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        path = '{0}{1}'.format('C', ':')
        self.getFile(os.listdir(path))
        self.nextPath=0
        #搜索得到的一个结果
        self.result = []
        #单击选中Click Select
        self.clickSelectList=[]
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        for attr in dir(self):
            if not attr.startswith('__') and 'pushButton' in attr:
                getattr(self, attr).setStyleSheet("border:none;")
        self.pushButton_2.clicked.connect(self.upload)
        self.pushButton.clicked.connect(self.download)
        self.pushButton_4.clicked.connect(self.share)
        self.pushButton_3.clicked.connect(self.delete)
        self.pushButton_5.clicked.connect(self.newfile)
        self.pushButton_9.clicked.connect(self.searchfile)
        self.pushButton_8.clicked.connect(self.back)
        self.pushButton_7.clicked.connect(self.forward)
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
        self.label_2.setText(_translate("MainWindow", "C:"))
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