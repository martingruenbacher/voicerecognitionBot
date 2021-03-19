import spotipy
from spotipy.oauth2 import SpotifyOAuth


SCOPE = 'streaming user-read-currently-playing user-read-playback-state'
CLIENT_ID = '8b8aa45522104448b5b17c41b8e395a2'
CLIENT_SECRET = 'f733c''1881bfc4712a28ae17d917f5fc8'
REDIRECT_URI = 'http://localhost:8888'

class Spotify():

    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPE))
        self.sp.shuffle(True)
        print(self.getDevices())
    
    def startSong(self):
        self.sp.start_playback()

    def pauseSong(self):
        self.sp.pause_playback()

    def skipSong(self):
        self.sp.next_track()

    def addToQueue(self, text):
        self.sp.add_to_queue(self.searchSong(text))

    def playSong(self, text):
        self.sp.start_playback(uris=[self.searchSong(text)])

    def playPlaylist(self, text):
        self.sp.start_playback(context_uri=self.searchPlaylist(text))

    def getDevices(self):
        dev = []
        for i in range(len(self.sp.devices()['devices'])):
            dev.append(self.sp.devices()['devices'][i]['name'])
        return dev

    def setMaxVolume(self):
        self.sp.volume(100)
    
    def setMinVolume(self):
        self.sp.volume(20)

    def searchSong(self, text):
        return self.sp.search(text, 1, 0, type='track')['tracks']['items'][-1]['uri']

    # searches user playlists
    def searchPlaylist(self, text):
        items = self.sp.current_user_playlists()['items']
        for i in range(len(items)):
            if items[i]['name'] == text:
                return items[i]['uri']
    

