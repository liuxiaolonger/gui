# -*- coding: utf-8 -*-
# @Time    : 2018\9\15 20:39
# @Author  : Tang weiyang
# @File    : FileSearch02.py
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
import os
import threading
from concurrent.futures import ThreadPoolExecutor
class fileSearchThread(QThread):
    sinOut = pyqtSignal(str)
    isAlive=False
    # 自定义信号，执行run()函数时，从相关线程发射此信号

    def __init__(self,key,path):
        super().__init__()
        self.key = key
        self.path=path

    def run(self):
        threads=[]
        #通过多线程对windows下的多个盘符进行文件的遍历查找
        pool = ThreadPoolExecutor(max_workers=5)
        list=[self.path]
        for each in list:
            t = threading.Thread(target=self.search, args=(self.key,each,))
            threads.append(t)
            t.start()

        for i in range(len(threads)): #将主线程阻塞
            threads[i].join()
        print("搜索结束")

    def search(self,keyword, path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if filename.__contains__(keyword):
                    print(os.path.join(dirpath, filename))
                    self.sinOut.emit(os.path.join(dirpath, filename))
            for folder in dirnames:
                if folder.__contains__(keyword):
                    print(os.path.join(dirpath,folder))
                    self.sinOut.emit(os.path.join(dirpath,folder))


class fileSearch(QListWidget):

    def __init__(self):
        super().__init__()
        self.Ui()

    def Ui(self):
        self.key= QLineEdit()
        self.bt=QPushButton("搜索")
        self.result = QListWidget()

        self.bt.clicked.connect(self.ButtonClicked) #按钮单击信号绑定到槽
        # self.line.editingFinished.connect(self.Action)
        self.key.editingFinished.connect(self.ButtonClicked)

        grid = QGridLayout()
        grid.setSpacing(10)  # 创建标签之间的空间

        grid.addWidget(self.key, 1, 0)  # （1,0）表示显示的位置
        grid.addWidget(self.bt, 1, 1)
        grid.addWidget(self.result, 2, 0, 5, 2)  # 指定组件的跨行和跨列的大小，指定这个元素跨5行显示

        self.setLayout(grid)
        for i in range(1,100):
            self.result.addItem("搜索"+str(i)+"个项目")

        self.result.itemClicked.connect(self.Clicked)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('文件搜索')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.show()

    def Clicked(self, item):
        QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())
        os.startfile(item.text()) #打开文件

    def ButtonClicked(self):
        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        keyword = self.key.text()
        self.result.clear()
        self.thread=fileSearchThread(keyword)
        self.thread.sinOut.connect(self.slotAdd)
        self.thread.start()

    def slotAdd(self,filename):

        self.result.addItem(str(filename))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = fileSearch()
    sys.exit(app.exec_())
