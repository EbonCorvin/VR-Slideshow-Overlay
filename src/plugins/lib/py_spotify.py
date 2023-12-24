import socket
import subprocess
import requests
import base64

TCP_IP = 'localhost'
TCP_PORT = 8888
CALLBACK_URL = "http://{}:{}/callback".format(TCP_IP, TCP_PORT)
BUFFER_SIZE = 1024

class pySpotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id;
        self.client_secret = client_secret;
        self.refresh_token = None;
        self.access_token =  None;

    def start_autho2(self, callback):
        # Simple local web server (For authorization)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((TCP_IP, TCP_PORT))
            s.listen(1)
        except Exception as ex:
            print(str(ex));
            exit();

        # print("Bind to port",TCP_PORT,"successfully");

        subprocess.run([
            "cmd",
            "/c",
            "start",
            "https://accounts.spotify.com/authorize?client_id="+self.client_id+"^&response_type=code^&redirect_uri="+CALLBACK_URL+"^&scope=user-read-currently-playing,user-modify-playback-state^&show_dialog=false"
        ])

        conn, addr = s.accept()
        # print ('Connection address:', addr)
        data = conn.recv(BUFFER_SIZE)
        dataArr = None
        if data:
            dataArr = data.decode().split("\r\n");
            # print(dataArr);
            conn.send(bytes("HTTP/1.1 200 OK\r\nConnection: close\r\n\r\nIt should work, you can close the browser now",'utf-8'))
            conn.close();
            s.close();
        code = dataArr[0][len("GET /callback?code="):-len(" HTTP/1.1")];
        # print("code", code)
        self.get_token(code = code);
        if callback is not None:
            callback();

    def get_token(self, isRefresh = False, code = None):
        data = {};
        if isRefresh:
            data["grant_type"] = "refresh_token"
            data["refresh_token"] = self.refresh_token
        else:
            data["grant_type"] = "authorization_code";
            data["redirect_uri"] = CALLBACK_URL;
            data["code"] = code;
        response = requests.post(
            "https://accounts.spotify.com/api/token",
            headers = {
                "Authorization": "Basic "+base64.b64encode((self.client_id+":"+self.client_secret).encode("utf-8")).decode("utf-8"),
                "Content-Type": "application/x-www-form-urlencoded"
            },
            data = data
        );
        if response.status_code == 200:
            data = response.json()
            if not isRefresh:
                self.refresh_token = data["refresh_token"];
            self.access_token = data["access_token"];
            # print("refresh_token", self.refresh_token,"access_token", self.access_token)

    def get_current_track(self):
        songResponse = requests.get(
            "https://api.spotify.com/v1/me/player/currently-playing",
            headers = {
                "Authorization": "Bearer "+self.access_token
            }
        )
        status_code = songResponse.status_code;
        # print(status_code)
        if status_code == 200:
            data = songResponse.json()
            isPlaying = "resuming" in data["actions"]["disallows"];
            isAd = data["currently_playing_type"]!="track";
            if isAd:
                return { "isPlaying": False, "trackName": "Listening to Spotify ad because I'm so broke" };
            artist = data["item"]["artists"][0]["name"];
            songName = data["item"]["name"];
            totalLen = data["item"]["duration_ms"];
            currentLen = data["progress_ms"];
            return { 
                "isPlaying": True, 
                "trackName": songName,
                "artist": artist,
                "isPaused": not isPlaying,
                "currentPos": currentLen,
                "totalLen": totalLen 
            };
        elif status_code == 204:
            return { "isPlaying": False, "trackName": "Spotify is not running" };
        else:
            print("Status code <> 200, will refresh token and try again");
            self.get_token(isRefresh = True);
            return self.get_current_track();

    def control_player(self):
        response = requests.post(
            "https://api.spotify.com/v1/me/player/next",
            headers = {
                "Authorization": "Bearer "+self.access_token
            }
        );
        # print(response)
        try:
            data = response.json();
            # print(data);
        except:
            print(response)
