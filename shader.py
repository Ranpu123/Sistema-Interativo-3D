from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GL import *

def LoadShader(vertex_path, fragment_path):
    with open(vertex_path) as f:
        vertex_src = f.readlines()
    
    with open(fragment_path) as f:
        fragment_src = f.readlines()

    shader = compileProgram(
        compileShader(vertex_src, GL_VERTEX_SHADER),
        compileShader(fragment_src, GL_FRAGMENT_SHADER)
    )

    return shader