import config;
from PIL import Image, ImageDraw, ImageFont, ImageColor;
import openvr;
import ctypes;
import time

config.add_general_setting_path("VROverlay (Experimental)", "output_ports.VROverlay")
config.addConfig("VROverlay (Experimental)", "IS_ENABLED", "Enable outputting to VROverlay?", "bool")

IS_ENABLED = False;
# TODO: Check if every Windows system has the font file "MSYH" (Microsoft YaHei)
FONT_NAME = "msyh.ttc";

TRANSPARENT = ImageColor.getrgb("#FFFFFF00");
OVERLAY_BACKGROUND = ImageColor.getrgb("#000000AA");

WIDTH = 400;
HEIGHT = 250
WIDTH_IN_METER = 0.15

font = None;
img = None;
draw = None
overlay = None;
handle = None;
vrSystem = None;
imageData = ctypes.c_buffer(b'', WIDTH * HEIGHT * 4);

def init():
    if openvr.isRuntimeInstalled()==0 or openvr.isHmdPresent()==0:
        raise Exception("This feature requires a VR headset!");
    initImage();
    initVROverlay();
    createOverlay();

def initImage():
    global font;
    global img;
    global draw;
    font = ImageFont.truetype(FONT_NAME, 24)
    img = Image.new("RGBA", (WIDTH,HEIGHT), 0);
    draw = ImageDraw.Draw(img);

def initVROverlay():
    global vrSystem;
    global overlay;
    try:
        vrSystem = openvr.init(openvr.VRApplication_Background);
        if vrSystem is None:
            raise Exception("No valid VR environment found");
        overlay=openvr.IVROverlay();
    except Exception as ex:
        translateAndRaiseError(ex);

def createOverlay():
    global overlay;
    global handle;
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

    handle=overlay.createOverlay("OSCChatBox_Overlay", "OSC Slideshow Overlay");
    # overlay.setOverlayTransformTrackedDeviceRelative(handle, openvr.k_unTrackedDeviceIndex_Hmd, arr);
    hand = vrSystem.getTrackedDeviceIndexForControllerRole(openvr.TrackedControllerRole_RightHand)
    overlay.setOverlayTransformTrackedDeviceRelative(handle, hand, arr);
    overlay.setOverlayAlpha(handle, 0.9)
    overlay.setOverlayWidthInMeters(handle, WIDTH_IN_METER);
    overlay.showOverlay(handle);

def translateAndRaiseError(ex):
    errType = type(ex);
    translation = errType.__name__;
    if errType==openvr.error_code.InitError_Init_NoServerForBackgroundApp:
        translation = "You're not in VR right now";
    elif errType==openvr.error_code.InitError_Init_HmdNotFound:
        translation = "Your headset hasn't connected to your PC yet";
    raise Exception(translation);

def outputString(text):
    global font;
    global img;
    global draw;
    global overlay;
    global imageData;
    global handle;
    text = "\n".join(text);
    text = text.replace("\v", "\n").replace("\t","  ")
    draw.rectangle([(0, 0), (WIDTH, HEIGHT)], TRANSPARENT);
    boundary = draw.textbbox((20,20),text, font);
    draw.rectangle([(1, 1), (boundary[2] - boundary[0] + 40 , boundary[3] - boundary[1] + 40)], OVERLAY_BACKGROUND, "black", 0);
    draw.text((20, 20), text, "white", font);
    imageBytes = img.tobytes();
    imageData.value = imageBytes;
    try:
        # Cause Request_Failed after a number of calls
        # Log Message: Refusing to create memory block because 201 blocks are already outstanding
        overlay.setOverlayRaw(handle, imageData, WIDTH, HEIGHT, 4)
    except Exception as ex:
        print(type(ex).__name__);
        if type(ex)==openvr.error_code.OverlayError_RequestFailed:
            # Not sure how to fix it, so the output will restart the overlay here
            openvr.shutdown();
            init();
            time.sleep(0.5)
            overlay.setOverlayRaw(handle, imageData, WIDTH, HEIGHT, 4)
        else:
            translateAndRaiseError(ex);
