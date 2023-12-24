"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from py_spotify import pySpotify;
from datetime import datetime;

CLIENT_ID = "9419b0b2a1874d21bfc77549aaf122f0"
CLIENT_SECRET = "b674009cd9874107bd89a7a3109ef25c";

spotifyClient = None;
lastBoopValue = 0
lastSkipSong = 0;
def start_osc_server():
  dispatcher = Dispatcher()
  dispatcher.map("/avatar/parameters/Boop", process_boop)
  server = osc_server.ThreadingOSCUDPServer(("127.0.0.1", 9001), dispatcher)
  print("Serving on {}".format(server.server_address))
  server.serve_forever()

def process_boop(addr, value):
  global lastBoopValue;
  global lastSkipSong;
  print(value, datetime.now().timestamp(), lastSkipSong);
  if value > 0.5 and datetime.now().timestamp() - lastSkipSong > 1.5:
      print("Boop!");
      lastSkipSong = datetime.now().timestamp();
      spotifyClient.control_player();
  lastBoopValue = value;

if __name__ == "__main__":
  spotifyClient = pySpotify(CLIENT_ID, CLIENT_SECRET);
  spotifyClient.start_autho2(start_osc_server);