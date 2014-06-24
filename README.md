# The Set Listener

This is the source for a web app called The Set Listener. The app
creates a Spotify playlist for your favorite artist's most recent
show. The app uses the Setlist.fm API and the Spotify API.

The app is online at [The Set Listener](http://static.echonest.com/SetListener)

<img src="http://static.echonest.com/SetListener/ss.png" width=600>


# The Server

The Set Listener has a server component that manages the API interaction with setlist.fm
because the setlist.fm API doesn't support cross-domain access.


# The Web App
The web app is a relatively simple app that solicits and artist name from the user, finds
recents shows by that artist via setlist.fm, looks up the Spotify tracks via the Spotify Web
API, and saves them to the user's Spotify Playlist after authorizing the user.

