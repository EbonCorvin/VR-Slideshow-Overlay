from pythonosc import udp_client
import config;

config.add_general_setting_path("VRCOsc", "output_ports.VRCOsc")
config.addConfig("VRCOsc", "IS_ENABLED", "Enable outputting to VRChat chatbox?", "bool")
config.addConfig("VRCOsc", "VRC_OSC_ADDR", "VRChat OSC Address", "str")
config.addConfig("VRCOsc", "VRC_OSC_PORT", "VRChat OSC Port", "num")

IS_ENABLED = True
VRC_OSC_PORT = 9000
VRC_OSC_ADDR = "127.0.0.1"
client = None;

def init():
    global client;
    client = udp_client.SimpleUDPClient(VRC_OSC_ADDR, VRC_OSC_PORT)

def outputString(text):
    global client;
    client.send_message("/chatbox/input",["\v".join(text),True]);
