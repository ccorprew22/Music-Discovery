## Known Problems/Acknowledgements

1. When parsing the JSON file sent through the Genius API, there are times when no url is found or it is provided with a url that redirects the user to a non-English speaking version of genius.com.
2. I would like to have implemented some kind of way for the user to save the song to their own Spotify playlist.

# Technical Issues
1. The artist history is shared across all users which is not supposed to happen.
2. Not every song had a song preview, which would break the app. So I wrote the function to either return None or a string with the preview url. If it was None, it would display an error message to the user.
3. 

# Known Problems
1. As of right now, the artist history is saved across all users. In the future I would try to make it so that each user gets their own history list.
2. 2. On mobile devices, the displays are responsive but are not centered correctly for each device size.

# How would improve my project
+ I would like to make it responsive amongst all devices, and I would like to connect it to user's spotify accounts so that they can add the song to their playlist.

# How to deploy

