# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtela/tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 761))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 271, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.listWidget_scene = QtWidgets.QListWidget(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_scene.sizePolicy().hasHeightForWidth())
        self.listWidget_scene.setSizePolicy(sizePolicy)
        self.listWidget_scene.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget_scene.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget_scene.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.listWidget_scene.setObjectName("listWidget_scene")
        self.verticalLayout_3.addWidget(self.listWidget_scene)
        self.pushB_removeIten = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushB_removeIten.setEnabled(False)
        self.pushB_removeIten.setObjectName("pushB_removeIten")
        self.verticalLayout_3.addWidget(self.pushB_removeIten)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.spinB_locationX = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_locationX.setMinimum(-999.99)
        self.spinB_locationX.setMaximum(999.99)
        self.spinB_locationX.setSingleStep(0.05)
        self.spinB_locationX.setObjectName("spinB_locationX")
        self.horizontalLayout_6.addWidget(self.spinB_locationX)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.spinB_locationY = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_locationY.setMinimum(-999.99)
        self.spinB_locationY.setMaximum(999.99)
        self.spinB_locationY.setSingleStep(0.05)
        self.spinB_locationY.setObjectName("spinB_locationY")
        self.horizontalLayout_6.addWidget(self.spinB_locationY)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.spinB_locationZ = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_locationZ.setMinimum(-999.99)
        self.spinB_locationZ.setMaximum(999.99)
        self.spinB_locationZ.setSingleStep(0.05)
        self.spinB_locationZ.setObjectName("spinB_locationZ")
        self.horizontalLayout_6.addWidget(self.spinB_locationZ)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.spinB_rotationX = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_rotationX.setMinimum(-999.99)
        self.spinB_rotationX.setMaximum(999.99)
        self.spinB_rotationX.setSingleStep(0.05)
        self.spinB_rotationX.setObjectName("spinB_rotationX")
        self.horizontalLayout_3.addWidget(self.spinB_rotationX)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.spinB_rotationY = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_rotationY.setMinimum(-999.99)
        self.spinB_rotationY.setMaximum(999.99)
        self.spinB_rotationY.setSingleStep(0.05)
        self.spinB_rotationY.setObjectName("spinB_rotationY")
        self.horizontalLayout_3.addWidget(self.spinB_rotationY)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.spinB_rotationZ = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_rotationZ.setMinimum(-999.99)
        self.spinB_rotationZ.setMaximum(999.99)
        self.spinB_rotationZ.setSingleStep(0.05)
        self.spinB_rotationZ.setObjectName("spinB_rotationZ")
        self.horizontalLayout_3.addWidget(self.spinB_rotationZ)
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAutoFillBackground(False)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        self.spinB_scaleX = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_scaleX.setMinimum(-999.99)
        self.spinB_scaleX.setMaximum(999.99)
        self.spinB_scaleX.setSingleStep(0.05)
        self.spinB_scaleX.setProperty("value", 1.0)
        self.spinB_scaleX.setObjectName("spinB_scaleX")
        self.horizontalLayout_4.addWidget(self.spinB_scaleX)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_4.addWidget(self.label_14)
        self.spinB_scaleY = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_scaleY.setMinimum(-999.99)
        self.spinB_scaleY.setMaximum(999.99)
        self.spinB_scaleY.setSingleStep(0.05)
        self.spinB_scaleY.setProperty("value", 1.0)
        self.spinB_scaleY.setObjectName("spinB_scaleY")
        self.horizontalLayout_4.addWidget(self.spinB_scaleY)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_4.addWidget(self.label_13)
        self.spinB_scaleZ = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.spinB_scaleZ.setMinimum(-999.99)
        self.spinB_scaleZ.setMaximum(999.99)
        self.spinB_scaleZ.setSingleStep(0.05)
        self.spinB_scaleZ.setProperty("value", 1.0)
        self.spinB_scaleZ.setObjectName("spinB_scaleZ")
        self.horizontalLayout_4.addWidget(self.spinB_scaleZ)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushB_selectColor = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushB_selectColor.setEnabled(True)
        self.pushB_selectColor.setAutoFillBackground(False)
        self.pushB_selectColor.setStyleSheet("background-color: rgb(120,120,120);")
        self.pushB_selectColor.setText("")
        self.pushB_selectColor.setObjectName("pushB_selectColor")
        self.horizontalLayout_7.addWidget(self.pushB_selectColor)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 540, 961, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.groupB_cameraType = QtWidgets.QGroupBox(self.groupBox)
        self.groupB_cameraType.setGeometry(QtCore.QRect(10, 20, 141, 111))
        self.groupB_cameraType.setObjectName("groupB_cameraType")
        self.radioB_perspective = QtWidgets.QRadioButton(self.groupB_cameraType)
        self.radioB_perspective.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioB_perspective.setChecked(True)
        self.radioB_perspective.setObjectName("radioB_perspective")
        self.cameraType_group = QtWidgets.QButtonGroup(MainWindow)
        self.cameraType_group.setObjectName("cameraType_group")
        self.cameraType_group.addButton(self.radioB_perspective)
        self.radioB_ortogonal = QtWidgets.QRadioButton(self.groupB_cameraType)
        self.radioB_ortogonal.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioB_ortogonal.setObjectName("radioB_ortogonal")
        self.cameraType_group.addButton(self.radioB_ortogonal)
        self.groupB_renderType = QtWidgets.QGroupBox(self.groupBox)
        self.groupB_renderType.setGeometry(QtCore.QRect(160, 20, 141, 111))
        self.groupB_renderType.setObjectName("groupB_renderType")
        self.radioB_polygon = QtWidgets.QRadioButton(self.groupB_renderType)
        self.radioB_polygon.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioB_polygon.setChecked(True)
        self.radioB_polygon.setObjectName("radioB_polygon")
        self.renderType_group = QtWidgets.QButtonGroup(MainWindow)
        self.renderType_group.setObjectName("renderType_group")
        self.renderType_group.addButton(self.radioB_polygon)
        self.radioB_line = QtWidgets.QRadioButton(self.groupB_renderType)
        self.radioB_line.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioB_line.setObjectName("radioB_line")
        self.renderType_group.addButton(self.radioB_line)
        self.radioB_point = QtWidgets.QRadioButton(self.groupB_renderType)
        self.radioB_point.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioB_point.setObjectName("radioB_point")
        self.renderType_group.addButton(self.radioB_point)
        self.horizontalLayout.addWidget(self.groupBox)
        self.gl_workspace = QtWidgets.QWidget(self.centralwidget)
        self.gl_workspace.setGeometry(QtCore.QRect(300, 10, 961, 521))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gl_workspace.sizePolicy().hasHeightForWidth())
        self.gl_workspace.setSizePolicy(sizePolicy)
        self.gl_workspace.setObjectName("gl_workspace")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAdd = QtWidgets.QMenu(self.menubar)
        self.menuAdd.setObjectName("menuAdd")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_OBJ = QtWidgets.QAction(MainWindow)
        self.actionOpen_OBJ.setObjectName("actionOpen_OBJ")
        self.actionPlane = QtWidgets.QAction(MainWindow)
        self.actionPlane.setObjectName("actionPlane")
        self.actionTriangle = QtWidgets.QAction(MainWindow)
        self.actionTriangle.setObjectName("actionTriangle")
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionCube = QtWidgets.QAction(MainWindow)
        self.actionCube.setObjectName("actionCube")
        self.actionPyramid = QtWidgets.QAction(MainWindow)
        self.actionPyramid.setObjectName("actionPyramid")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.menuFile.addAction(self.actionOpen_OBJ)
        self.menuAdd.addAction(self.actionPlane)
        self.menuAdd.addAction(self.actionTriangle)
        self.menuAdd.addAction(self.actionSquare)
        self.menuAdd.addSeparator()
        self.menuAdd.addAction(self.actionCube)
        self.menuAdd.addAction(self.actionPyramid)
        self.menuAdd.addSeparator()
        self.menuAdd.addAction(self.actionLight)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAdd.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema Interativo 3D - 2023"))
        self.label.setText(_translate("MainWindow", "Scene:"))
        self.pushB_removeIten.setText(_translate("MainWindow", "Remove"))
        self.label_2.setText(_translate("MainWindow", "Transformations"))
        self.label_6.setText(_translate("MainWindow", "Translate:"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", "Z"))
        self.label_7.setText(_translate("MainWindow", "Rotation:"))
        self.label_11.setText(_translate("MainWindow", "X"))
        self.label_9.setText(_translate("MainWindow", "Y"))
        self.label_10.setText(_translate("MainWindow", "Z"))
        self.label_8.setText(_translate("MainWindow", "Scale:"))
        self.label_12.setText(_translate("MainWindow", "X"))
        self.label_14.setText(_translate("MainWindow", "Y"))
        self.label_13.setText(_translate("MainWindow", "Z"))
        self.label_15.setText(_translate("MainWindow", "Color:"))
        self.groupBox.setTitle(_translate("MainWindow", "Extra"))
        self.groupB_cameraType.setTitle(_translate("MainWindow", "Camera Type"))
        self.radioB_perspective.setText(_translate("MainWindow", "Perpesctive"))
        self.radioB_ortogonal.setText(_translate("MainWindow", "Orthogonal"))
        self.groupB_renderType.setTitle(_translate("MainWindow", "Render Type"))
        self.radioB_polygon.setText(_translate("MainWindow", "Polygon"))
        self.radioB_line.setText(_translate("MainWindow", "Line"))
        self.radioB_point.setText(_translate("MainWindow", "Point"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAdd.setTitle(_translate("MainWindow", "Add"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen_OBJ.setText(_translate("MainWindow", "Open .OBJ"))
        self.actionPlane.setText(_translate("MainWindow", "Plane"))
        self.actionTriangle.setText(_translate("MainWindow", "Triangle"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionCube.setText(_translate("MainWindow", "Cube"))
        self.actionPyramid.setText(_translate("MainWindow", "Pyramid"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
