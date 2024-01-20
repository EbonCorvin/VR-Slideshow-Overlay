import config;
from PIL import Image, ImageDraw, ImageFont, ImageColor;
import openvr;
import ctypes;

config.add_general_setting_path("VROverlay (Experimental)", "output_ports.VROverlay")
config.addConfig("VROverlay (Experimental)", "IS_ENABLED", "Enable outputting to VROverlay?", "bool")

IS_ENABLED = False;
# TODO: Check if every Windows system has the font file "MSYH" (Microsoft YaHei)
FONT_NAME = "msyh.ttc";

TRANSPARENT = ImageColor.getrgb("#FFFFFF00");

WIDTH = 400;
HEIGHT = 250
WIDTH_IN_METER = 0.15

font = None;
img = None;
draw = None
overlay = None;
handle = None;

def init():
    global font;
    global img;
    global draw;
    global overlay;
    global handle;

    font = ImageFont.truetype(FONT_NAME, 24)
    img = Image.new("RGBA", (WIDTH,HEIGHT), 0);
    draw = ImageDraw.Draw(img);

    vrSystem = openvr.init(openvr.VRApplication_Background);
    overlay=openvr.IVROverlay();
    handle=overlay.createOverlay("OSCChatBox_Overlay", "OSC Slideshow Overlay");
    overlay.setOverlayWidthInMeters(handle, WIDTH_IN_METER);
    arr = openvr.HmdMatrix34_t()

    # https://www.brainvoyager.com/bv/doc/UsersGuide/CoordsAndTransforms/SpatialTransformationMatrices.html
    # Position
    arr[0][0] = 1
    arr[1][1] = 1
    arr[2][2] = 1
    
    arr[0][3] = 0;      # X
    arr[1][3] = 0.05;   # Y
    arr[2][3] = 0       # Z 

    # Rotation
    arr[0][0] = 1
    arr[1][0] = 0
    arr[2][0] = 0

    arr[0][1] = 0
    arr[1][1] = 0
    arr[2][1] = -1

    arr[0][2] = 0
    arr[1][2] = 1
    arr[2][2] = 0

    # overlay.setOverlayTransformTrackedDeviceRelative(handle, openvr.k_unTrackedDeviceIndex_Hmd, arr);
    hand = vrSystem.getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_RightHand)
    overlay.setOverlayTransformTrackedDeviceRelative(handle, hand, arr);
    overlay.showOverlay(handle);

def outputString(text):
    global font;
    global img;
    global draw;
    global overlay;
    global handle;
    text = "\n".join(text);
    text = text.replace("\v", "\n").replace("\t","  ")
    draw.rectangle([(0, 0), (WIDTH, HEIGHT)], TRANSPARENT);
    boundary = draw.textbbox((20,20),text, font);
    draw.rectangle([(0, 0), (boundary[2] - boundary[0] + 40 , boundary[3] - boundary[1] + 40)], "black");
    draw.text((20, 20), text, "white", font);
    imageData = img.tobytes();
    overlay.setOverlayRaw(handle, ctypes.c_buffer(imageData, len(imageData)), WIDTH, HEIGHT, 4)

