from constants import *
import pyglet,os

__all__ = ['mouse', 'pmouse', 'attrib', 'frame', 'key', 'canvas', 'shape', 
           'screen', 'config', 'callback']

#************************
#  GLOBALS
#************************
class mouse:
    """Stores mouse state"""
    pressed = False # Tells if any mouse button is pressed
    x = 0 # x coordinate of mouse
    y = 0 # y coordinate of mouse
    button = None # state of mouse buttons

class pmouse:
    """Store previous position of mouse"""
    pressed = False # Tells if any mouse button is pressed
    x = 0 # x coordinate of mouse
    y = 0 # y coordinate of mouse
    savex = 0 # saved x from the previous frame
    savey = 0 # saved y from the previous frame
    button = None # state of mouse buttons
    
class key:
    """Stores keyboard state"""
    char = ""
    code = 0
    modifiers = None
    pressed = False

class canvas:
    """Stores the drawing window attributes"""
    window = None 
    # These two symbols were relocated to the __builtin__ namespace
    #width = 100
    #height = 100
    
class screen:
    """Current window properties."""
    width = None
    height = None
    
class attrib:
    """Drawing attributes"""
    strokeColor = (0,0,0,1)
    fillColor = (1,1,1,1)
    tintColor = None
    strokeWeight = 1
    font = {}
    location = pyglet.resource.FileLocation(os.path.dirname(__file__))
    
    rectMode = CORNER
    ellipseMode = CENTER
    textAlign = (LEFT,BASELINE)
    # color attribs
    colorMode = RGB
    colorRange = (255.0,255.0,255.0,255.0)
    # light attribs
    lights = False
    lightCount = 0
    lightSpecular = (0,0,0,1)
    lightFalloff = (1, 0, 0) # constant, linear, quadratic
    # depth testing
    depthTest = True

class frame:
    """Frame rate and the like."""
    loop=True
    rate=10 # estimated frame rate
    targetRate = 60 # the target frame rate
    count=0 # number of frames displayed since the application started
    
class shape:
    """Attributes for shapes."""
    quadric = None
    tess = gl.gluNewTess()
    ellipseFillDL = None
    ellipseStrokeDL = None
    type = None
    sphereDetail = (20,10)
    bezierDetail = 20
    curveDetail = 20
    ellipseDetail = 100
    tension = 0.5
    bezierBlend = []
    vtx = []
    nrm = []

class config:
    """Configuration variables for the library."""
    # whether or not to invert the y axis. This requires fixing the drawing of 
    # some primitives such as arc or text
    coordInversionHack = True 
    # try to get around the artifacts when drawing filled polygons in smooth mode
    smoothFixHack = False # off by default 
    smoothTurnedOn = False # Used internally to tell whether smooth was on
    # flipping policy
    flipPolicy = DOUBLE_FLIP_POLICY # this is the default and should work for modern boards/drivers
    # flipPolicy = SINGLE_FLIP_POLICY # use this for Intel 945 under Windows or other cheap boards
    # flipPolicy = FBO_FLIP_POLICY # use this for modern boards/drivers where flip uses swap and not copy
    # flipPolocy = ACCUM_FLIP_POLICY # use this for cheap boards where 'SINGLE' produces too much flickering
    
class callback:
    """Call back functions."""
    
    @staticmethod
    def dummy(*args):
        """A callback function that does nothing."""
        pass
        
    """All of these are imported from the user space
    by the 'run' function or else fall back to dummy"""
    draw = mousePressed = mouseReleased = mouseClicked = mouseDragged = \
           mouseMoved = keyPressed = keyReleased = keyTyped = exit = \
           screenResized = dummy

