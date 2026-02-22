import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Cube vertices
vertices = (
    (-1, -1, -1),
    ( 1, -1, -1),
    ( 1,  1, -1),
    (-1,  1, -1),
    (-1, -1,  1),
    ( 1, -1,  1),
    ( 1,  1,  1),
    (-1,  1,  1)
)

edges = (
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
)

# Pyramid (roof)
pyramid_faces = (
    (4,5,8),
    (5,6,8),
    (6,7,8),
    (7,4,8)
)

apex = (0, 0, 2)

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def pyramid():
    glBegin(GL_TRIANGLES)
    for face in pyramid_faces:
        for vertex in face:
            if vertex == 8:
                glVertex3fv(apex)
            else:
                glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    glTranslatef(0, 0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotatef(1, 0, 1, 0)
        glPushMatrix()
        glScalef(2, 2, 2)
        cube()
        glPopMatrix()

        # Translation for roof
        glPushMatrix()
        glTranslatef(0, 1, 0)
        pyramid()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()
# use code below to run the code
#py -3.12 "c:/Users/Lenovo/OneDrive/Desktop/COMPUTER GRAPHICS/last lab/1st qn .py"
#>>      and leave the # do not use it in the terminal