from Spotify import Spotify


sp = Spotify()
sp.getDevices()
sp.startSong()
sp.skipSong()
sp.playPlaylist("Italien 2020")
#sp.addToQueue("ischgl fieber")
sp.setMaxVolume()