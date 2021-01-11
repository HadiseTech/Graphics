
import sys, pygame

from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import os

# IMPORT OBJECT LOADER
from objloader import *
def load_sound(filename):
    return pygame.mixer.Sound(os.path.join('sounds', filename))

pygame.init()
viewport = (1200,700)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded
# LOAD OBJECT AFTER PYGAME INIT
obj = OBJ('rr.obj', swapyz=True)
clock = pygame.time.Clock()
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (6,6)
tx, ty = (0,0)
zpos = -5
ypos =5
xpos = 5
rotate = move = False
counter = 0
x = 1
y =1
soundtrac = load_sound('soundtrack.wav')
inc =1
z1 =0
z2 =0
while 1:
    soundtrac.play()
    clock.tick(30)
    keys = pygame.key.get_pressed()
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
                print("rx =",rx)
                print('ry =',rx)
                print("tx =",tx)
                print("ty =",ty)
            if move:
                tx += i
                ty -= j
                print("tx =",tx)
                print("ty =",ty)
                print("rx =",rx)
                print('ry =',rx)
        elif keys[pygame.K_UP]:
            zpos +=2
        elif keys[pygame.K_DOWN]:
            zpos -=2
        elif keys[pygame.K_LEFT]:
            xpos +=2
        elif keys[pygame.K_RIGHT]:
            xpos -=2
        elif keys[pygame.K_c]:
            ypos -=2
        elif keys[pygame.K_v]:
            ypos +=2
            counter -=5
        if keys[pygame.K_m]:
            z1+=1
        if keys[pygame.K_n]:
           z2 +=1
           
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # RENDER OBJECT
    glTranslate(tx-xpos, ty-ypos, - zpos-20)
    glRotate(ry, x, 0, z1)
    glRotate(rx, 0, y, z2)
    glCallList(obj.gl_list)

    

    zpos-=0.1
    
    counter+=1
    

    pygame.display.flip()
