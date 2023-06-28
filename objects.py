from OpenGL.GL import *
import numpy as np
import pyrr

class OBJ:
    def __init__(self):
        self.vertices = None
        self.normals = None
        self.name = "Default"
        self.position = np.array([0,0,0],np.float32)
        self.scale = np.array([1,1,1],np.float32)
        self.rotation = np.array([0,0,0],np.float32)
        self.color = np.array([0.47,0.47,0.47],np.float32)
        self.vao = None
        self.vbo = None
        self.isInit = False

    def initializeArrays(self):
        self.vertices = np.array(self.vertices, dtype=np.float32)
        self.vertice_count = len(self.vertices)//3
        self.vao = glGenVertexArrays(1)
        self.vbo = glGenBuffers(1)
        
        glBindVertexArray(self.vao)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)

        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, ctypes.c_void_p(0))

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

        self.isInit = True

    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))
    
    def getModelMatrix(self):
        model_matrix = pyrr.matrix44.create_identity()
        position = pyrr.Vector3(self.position)
        rotation = pyrr.Quaternion.from_eulers(np.radians(self.rotation))
        scale = pyrr.Vector3(self.scale)

        translation_matrix = pyrr.matrix44.create_from_translation(position)
        rotation_matrix = pyrr.matrix44.create_from_quaternion(rotation)
        scale_matrix = pyrr.matrix44.create_from_scale(scale)

        
        model_matrix = pyrr.matrix44.multiply(model_matrix, scale_matrix)
        model_matrix = pyrr.matrix44.multiply(model_matrix, rotation_matrix)
        model_matrix = pyrr.matrix44.multiply(model_matrix, translation_matrix)

        return model_matrix

class Camera():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.aspect = self.w/self.h
        self.position = np.array([0,0,-2],np.float32)
        self.up = np.array([0,-1,0],np.float32)
        self.facing = np.array([0,0,1],np.float32)
        self.phi = 0
        self.theta = 90
        self.cameraType = False
        self.draw = GL_TRIANGLES
        self.updateFacing()

    def getProjectionMatrix(self):
        if self.cameraType:
            self.projection_matrix = pyrr.Matrix44.orthogonal_projection(-1, 1, -1, 1, 0.1, 100, np.float32)
        else:
            self.projection_matrix = pyrr.Matrix44.perspective_projection(45, self.aspect, 0.1, 100, np.float32)

        return self.projection_matrix

    def getViewMatrix(self):
        self.view_matrix = pyrr.Matrix44.look_at(self.position, self.position + self.facing, self.up, np.float32)
        return self.view_matrix
    
    def updateFacing(self):
        self.facing = np.array([
            np.cos(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi)),    
            np.sin(np.deg2rad(self.phi)),
            np.sin(np.deg2rad(self.theta)) * np.cos(np.deg2rad(self.phi))
        ])
        globalup = np.array([0,-1,0])
        self.facing = pyrr.vector3.normalise(self.facing)
        self.right = pyrr.vector3.normalise(np.cross(globalup, self.facing))
        self.up = pyrr.vector3.normalise(np.cross(self.right, self.facing))

    def spinCamera(self, dTheta, dPhi):
        self.theta += dTheta
        if self.theta > 360:
            self.theta -= 360
        elif self.theta < 0:
            self.theta += 360

        self.phi = min(
            89, max(-89, self.phi + dPhi)
        )

        self.updateFacing()
    
class Cube(OBJ):
    class_id = 0
    def __init__(self):
        super(Cube, self).__init__()
        Cube.class_id += 1
        self.id = Cube.class_id
        self.name = f"Cube({self.id})"
        self.vertices = [   -0.5, -0.5, -0.5, 
                             0.5, -0.5, -0.5,  
                             0.5,  0.5, -0.5,  
                             0.5,  0.5, -0.5,  
                            -0.5,  0.5, -0.5, 
                            -0.5, -0.5, -0.5, 

                            -0.5, -0.5,  0.5, 
                             0.5, -0.5,  0.5,  
                             0.5,  0.5,  0.5,  
                             0.5,  0.5,  0.5,  
                            -0.5,  0.5,  0.5, 
                            -0.5, -0.5,  0.5, 

                            -0.5,  0.5,  0.5, 
                            -0.5,  0.5, -0.5, 
                            -0.5, -0.5, -0.5, 
                            -0.5, -0.5, -0.5, 
                            -0.5, -0.5,  0.5, 
                            -0.5,  0.5,  0.5, 

                             0.5,  0.5,  0.5,  
                             0.5,  0.5, -0.5,  
                             0.5, -0.5, -0.5,  
                             0.5, -0.5, -0.5,  
                             0.5, -0.5,  0.5,  
                             0.5,  0.5,  0.5,  

                            -0.5, -0.5, -0.5, 
                             0.5, -0.5, -0.5,  
                             0.5, -0.5,  0.5,  
                             0.5, -0.5,  0.5,  
                            -0.5, -0.5,  0.5, 
                            -0.5, -0.5, -0.5, 

                            -0.5,  0.5, -0.5, 
                             0.5,  0.5, -0.5,  
                             0.5,  0.5,  0.5,  
                             0.5,  0.5,  0.5,  
                            -0.5,  0.5,  0.5, 
                            -0.5,  0.5, -0.5,]

class Plane(OBJ):
    class_id = 0
    def __init__(self):
        super(Plane, self).__init__()
        Plane.class_id += 1
        self.id = Plane.class_id
        self.name = f"Plane({self.id})"
        self.vertices = [   -0.5,0.0,-0.5,
                             0.5,0.0,-0.5,
                             0.5,0.0,0.5,
                            -0.5,0.0,-0.5,
                            
                            -0.5,0.0,0.5,
                             0.5,0.0,0.5,
                            -0.5,0.0,-0.5,
                            -0.5,0.0,0.5,
                        ]
        
class Triangle(OBJ):
    class_id = 0
    def __init__(self):
        super(Triangle, self).__init__()
        Triangle.class_id += 1
        self.id = Triangle.class_id
        self.name = f"Triangle({self.id})"
        self.vertices = [   -0.5,0.0,0.0,
                             0.5,0.0,0.0,
                             0.0,0.5,0.0,
                            -0.5,0.0,0.0,
                        ]

