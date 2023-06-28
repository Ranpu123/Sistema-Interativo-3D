import sys
from PyQt5.Qt import Qt
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtOpenGL
from PyQt5.QtCore import QEvent, QObject

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QOpenGLWidget, QVBoxLayout, QColorDialog, QStyle
)
from OpenGL.GL import *
from OpenGL.GLUT import *
from ui import Ui_MainWindow
from objects import Cube, Camera, Plane, Triangle
import shader
import pyrr
import numpy as np

camera = None

class GLWidget(QOpenGLWidget):
    init = QtCore.pyqtSignal()
    render_file = []

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.setMouseTracking(True)
        self.last_x = 0
        self.last_y = 0
        self.spinFlag = False
        self.render_file = []
        
    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glLineWidth(2)
        glPointSize(5)
        glClearColor(0,0,0,1)
        self.setupShader()
        self.render_file.append(Cube())
        self.init.emit()
        print(f"Current Version: {glGetString(GL_VERSION)}")
        
    def resizeGL(self, width, height):
        glViewport(0,0,width,height)

    def paintGL(self):
        glClearColor(0,0,0,1)
        self.renderList()
    
    def setupShader(self):
        self.shaderP = shader.LoadShader("SimpleVertexShader.vertexshader", "SimpleFragmentShader.fragmentshader")
        self.Model_matrix = glGetUniformLocation(self.shaderP,"Model")
        self.Projection_matrix = glGetUniformLocation(self.shaderP,"Projection")
        self.View_matrix = glGetUniformLocation(self.shaderP,"View")
        self.Color = glGetUniformLocation(self.shaderP,"Color")
    
    def renderList(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.shaderP)
        projection = camera.getProjectionMatrix()
        view = camera.getViewMatrix()

        for item in self.render_file:
            if item.isInit:
                glUniformMatrix4fv(self.Model_matrix,1,GL_FALSE,item.getModelMatrix())
                glUniformMatrix4fv(self.Projection_matrix,1,GL_FALSE,projection)
                glUniformMatrix4fv(self.View_matrix,1,GL_FALSE,view)
                glUniform3fv(self.Color,1,item.color)
                glBindVertexArray(item.vao)
                glDrawArrays(camera.draw,0,item.vertice_count)
                glBindVertexArray(0)
            else:
                item.initializeArrays()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.spinFlag = False

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:    
            self.last_x = event.pos().x()
            self.last_y = event.pos().y()
            self.spinFlag = True

    def mouseMoveEvent(self, event):
        if self.spinFlag:    
            theta_increment = 0.2*(self.last_x - event.pos().x())
            phi_increment = 0.2*(self.last_y - event.pos().y())
            self.last_x = event.pos().x()
            self.last_y = event.pos().y()
            camera.spinCamera(theta_increment, -phi_increment)
        
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setupOpenGLWidget()
        self.viewport.init.connect(self.onGLInit)

        self.setMouseTracking(True)

        self.cameraType_group.buttonClicked[int].connect(self.changeCameraType)
        self.renderType_group.buttonClicked[int].connect(self.changeRenderType)

        self.actionCube.triggered.connect(self.addCube)
        self.actionPlane.triggered.connect(self.addPlane)
        self.actionTriangle.triggered.connect(self.addTriangle)

        self.pushB_removeIten.clicked.connect(self.removeItem)
        self.listWidget_scene.itemClicked.connect(self.loadItemToUI)

        self.spinB_locationX.valueChanged.connect(self.itemUpdated)
        self.spinB_locationY.valueChanged.connect(self.itemUpdated)
        self.spinB_locationZ.valueChanged.connect(self.itemUpdated)

        self.spinB_scaleX.valueChanged.connect(self.itemUpdated)
        self.spinB_scaleY.valueChanged.connect(self.itemUpdated)
        self.spinB_scaleZ.valueChanged.connect(self.itemUpdated)

        self.spinB_rotationX.valueChanged.connect(self.itemUpdated)
        self.spinB_rotationY.valueChanged.connect(self.itemUpdated)
        self.spinB_rotationZ.valueChanged.connect(self.itemUpdated)

        self.pushB_selectColor.clicked.connect(self.setItemColor)

    def onGLInit(self):
        global camera 
        camera = Camera(self.viewport.width(), self.viewport.height())
        self.loadToListWidget()
        timer = QtCore.QTimer(self)
        timer.setInterval(16)
        timer.timeout.connect(self.viewport.update)
        timer.start()
        self.currentItem = 0
    
    def setItemColor(self):
        color = QColorDialog().getColor(QtGui.QColor(Qt.white),self, title="Escolha a cor")
        item = self.viewport.render_file[self.currentItem]
        rgb = color.getRgb()
        if color.isValid():
            item.color[0] = rgb[0]/255
            item.color[1] = rgb[1]/255
            item.color[2] = rgb[2]/255
        self.pushB_selectColor.setStyleSheet(f"background-color: rgb({rgb[0]},{rgb[1]},{rgb[2]});")

    def changeCameraType(self, id):
        for button in self.cameraType_group.buttons():
            if id == -3:
                camera.cameraType = True
            else:
                camera.cameraType = False
    
    def changeRenderType(self, id):
        for button in self.renderType_group.buttons():
            if id == -2:
                camera.draw = GL_TRIANGLES
            elif id == -3:
                camera.draw = GL_LINE_STRIP
            else:
                camera.draw = GL_POINTS

    def addCube(self):
        self.viewport.render_file.append(Cube())
        self.addingObjectScene()
    
    def addPlane(self):
        self.viewport.render_file.append(Plane())
        self.addingObjectScene()

    def addTriangle(self):
        self.viewport.render_file.append(Triangle())
        self.addingObjectScene()    

    def addingObjectScene(self):
        self.listWidget_scene.addItem(self.viewport.render_file[-1].name)
        self.currentItem = self.listWidget_scene.count()-1
        self.listWidget_scene.setCurrentRow(self.currentItem)
        self.pushB_removeIten.setEnabled(True)
        self.TransformationSignals(True)
        self.loadItemToUI()  
        self.TransformationSignals(False)
    
    def TransformationSignals(self, flag):
        self.spinB_locationX.blockSignals(flag)
        self.spinB_locationY.blockSignals(flag)
        self.spinB_locationZ.blockSignals(flag)

        self.spinB_rotationX.blockSignals(flag)
        self.spinB_rotationY.blockSignals(flag)
        self.spinB_rotationZ.blockSignals(flag)

        self.spinB_scaleX.blockSignals(flag)
        self.spinB_scaleY.blockSignals(flag)
        self.spinB_scaleZ.blockSignals(flag)

    def loadToListWidget(self):
        self.pushB_removeIten.setEnabled(False)
        self.listWidget_scene.clear()
        if len(self.viewport.render_file) > 0:
            for item in self.viewport.render_file:
                self.listWidget_scene.addItem(item.name)
            self.listWidget_scene.setCurrentRow(0)
            self.currentItem = 0
            self.pushB_removeIten.setEnabled(True)
    
    def loadItemToUI(self):
        self.currentItem = self.listWidget_scene.currentRow()
        item = self.viewport.render_file[self.currentItem]
        self.TransformationSignals(True)
        self.spinB_locationX.setValue(item.position[0])
        self.spinB_locationY.setValue(item.position[1])
        self.spinB_locationZ.setValue(item.position[2])

        self.spinB_rotationX.setValue(item.rotation[0])
        self.spinB_rotationY.setValue(item.rotation[1])
        self.spinB_rotationZ.setValue(item.rotation[2])

        self.spinB_scaleX.setValue(item.scale[0])
        self.spinB_scaleY.setValue(item.scale[1])
        self.spinB_scaleZ.setValue(item.scale[2])
        self.TransformationSignals(False)

        self.pushB_selectColor.setStyleSheet(f"background-color: rgb({item.color[0]},{item.color[1]},{item.color[2]});")

    
    def itemUpdated(self):
        self.currentItem = self.listWidget_scene.currentRow()
        item = self.viewport.render_file[self.currentItem]

        item.position[0] = self.spinB_locationX.value()
        item.position[1] = self.spinB_locationY.value()
        item.position[2] = self.spinB_locationZ.value()

        item.rotation[0] = self.spinB_rotationX.value()
        item.rotation[1] = self.spinB_rotationY.value()
        item.rotation[2] = self.spinB_rotationZ.value()

        item.scale[0] = self.spinB_scaleX.value()
        item.scale[1] = self.spinB_scaleY.value()
        item.scale[2] = self.spinB_scaleZ.value()

    def setupOpenGLWidget(self):
        self.viewport = GLWidget(self) 
        layout = QVBoxLayout()
        layout.addWidget(self.viewport)
        self.gl_workspace.setLayout(layout)
    
    def removeItem(self):
        if len(self.viewport.render_file) > 0:
            self.viewport.render_file.pop(self.currentItem)
            self.loadToListWidget()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())