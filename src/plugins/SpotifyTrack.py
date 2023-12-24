import math
from plugins.lib import py_spotify
import config;

CLIENT_ID = "SPOTIFY_CIENT_ID"
CLIENT_SECRET = "SPOTIFY_SECRET";
SONG_CHAT_TEXT_FORMAT = "Currently playing on Spotify:\v{} - {}{}";

MODULE_NAME = "GetSpotifyTrack";
MODULE_DESC = "Show current Spotify track"

config.addConfig(__name__, "CLIENT_ID", "Your Spotify developer client ID.", "str")
config.addConfig(__name__, "CLIENT_SECRET", "Your Spotify developer client secret code.", "str")

class SpotifyTrack:
    updateRate = 7;
    refreshInterval = 5;
    refreshTriggerCount = 0;
    refreshTrackCounter = 0;
    trackInfo = None;

    def __init__(self):
        self.refreshTriggerCount = math.floor(self.refreshInterval / self.updateRate);
    
    def init(self):
        self.spotifyClient = py_spotify.pySpotify(CLIENT_ID, CLIENT_SECRET);
        self.spotifyClient.start_autho2(None);

    def onUpdate(self, scriptUpTime):
        spotifyClient = self.spotifyClient;
        if self.refreshTrackCounter==0:
            trackInfo = spotifyClient.get_current_track();
            # print(trackInfo);
            self.trackInfo = trackInfo;
            if trackInfo["isPlaying"]:
                totalLen = trackInfo["totalLen"];
                currentPos = trackInfo["currentPos"];
                remaining = (totalLen - currentPos) / 1000;
                if remaining <= self.refreshInterval:
                    # print(
                    #     self.refreshInterval, 
                    #     remaining, 
                    #     self.refreshTriggerCount,
                    #     math.floor(self.refreshTriggerCount * ((self.refreshInterval - remaining) / self.refreshInterval))
                    # )
                    self.refreshTrackCounter = math.floor(self.refreshTriggerCount * ((self.refreshInterval - remaining) / self.refreshInterval));
        else:
            if self.trackInfo["isPlaying"] and not self.trackInfo["isPaused"]:
                self.trackInfo["currentPos"] += self.updateRate * 1000;
                # print(self.trackInfo["currentPos"]);

        self.refreshTrackCounter+=1;
        # print(self.refreshTrackCounter)
        if self.refreshTrackCounter > self.refreshTriggerCount:
            self.refreshTrackCounter = 0;
        return self.format_track_info();

    def format_track_info(self):
        if self.trackInfo["isPlaying"]:
            trackText = SONG_CHAT_TEXT_FORMAT.format(
                self.trackInfo["trackName"],
                self.trackInfo["artist"],
                ""
                # " (Pause)" if self.trackInfo["isPaused"] else ""
            );
            progressbar = "";
            if self.trackInfo["isPaused"]:
                progressbar = "├──Paused──┤";
            else:
                progressbar = "├" + ("─" * 10) + "┤";
                index = min(10,math.floor(self.trackInfo["currentPos"] / self.trackInfo["totalLen"] * 10) + 1);
                progressbar = progressbar[:index] + "■" + progressbar[index+1:]
            return trackText + "\v" + progressbar;
        else:
            return self.trackInfo["trackName"]
